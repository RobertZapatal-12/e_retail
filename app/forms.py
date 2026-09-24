"""Form definitions shared with the existing repository insertion methods."""

import inspect
import re
from datetime import datetime
from decimal import Decimal, InvalidOperation

from repositories.customers_repo import CustomersRepository
from repositories.orders_repo import OrdersRepository
from repositories.payments_repo import PaymentsRepository
from repositories.product_repo import ProductRepository


GROUPS = {
    "Catálogo": (ProductRepository, {
        "Productos": "insert_product", "Marcas": "insert_brands",
        "Categorías": "insert_category", "Categorías de producto": "insert_productcategories",
        "Variantes": "insert_productvarints", "Atributos": "insert_product_attribute_keys",
        "Valores de atributos": "insert_variant_attribute_values",
        "Proveedores": "insert_suppliers", "Proveedores de producto": "insert_product_suppliers",
        "Tiendas": "insert_stores", "Inventario": "insert_inventory",
        "Movimientos": "insert_inventory_transactions",
    }),
    "Clientes": (CustomersRepository, {
        "Clientes": "insert_customers", "Direcciones": "insert_customer_addresses",
    }),
    "Pedidos": (OrdersRepository, {
        "Pedidos": "insert_orders", "Estados de pedido": "insert_order_statuses",
        "Detalle de pedido": "insert_order_items", "Transportistas": "insert_carriers",
        "Envíos": "insert_shipments", "Estados de envío": "insert_shipment_statuses",
        "Promociones": "insert_promotions", "Tipos de promoción": "insert_promotion_types",
        "Promociones de pedido": "insert_order_promotions",
    }),
    "Pagos": (PaymentsRepository, {
        "Pagos": "insert_payments", "Métodos de pago": "insert_payment_methods",
        "Estados de pago": "insert_payment_statuses", "Monedas": "insert_currencies",
    }),
}

LABELS = dict(line.split("=", 1) for line in """name=Nombre
description=Descripción
sku=SKU
first_name=Nombres
last_name=Apellidos
email=Correo electrónico
phone=Teléfono
code=Código
slug=Slug
price=Precio de venta
cost_price=Precio de costo
weight_kg=Peso (kg)
label=Etiqueta
value=Valor
contact_name=Persona de contacto
address=Dirección
supplier_sku=SKU del proveedor
lead_time_days=Plazo de entrega (días)
location_name=Sucursal
address_line1=Dirección, línea 1
address_line2=Dirección, línea 2
city=Ciudad
state=Provincia / estado
postal_code=Código postal
country=País
quantity_on_hand=Existencias
quantity_reserved=Cantidad reservada
minimum_level=Nivel mínimo
transaction_type=Tipo de movimiento
quantity=Cantidad
source=Origen
notes=Notas
order_number=Número de pedido
currency_code=Código de moneda
unit_price=Precio unitario
line_total=Total de línea
tax_amount=Impuesto
discount_amount=Descuento
contact_info=Información de contacto
tracking_number=Número de seguimiento
shipped_at=Fecha de envío
estimated_delivery_at=Entrega estimada
delivered_at=Fecha de entrega
shipping_amount=Costo de envío
starts_at=Fecha de inicio
ends_at=Fecha de fin
provider=Proveedor de pago
amount=Importe
transaction_reference=Referencia de transacción
brand_id=ID de marca
product_id=ID de producto
category_id=ID de categoría
parent_category_id=ID de categoría superior
variant_id=ID de variante
attribute_key_id=ID de atributo
variant_attribute_value_id=ID del valor de atributo
supplier_id=ID de proveedor
store_id=ID de tienda
inventory_id=ID de inventario
transaction_id=ID de movimiento
reference_id=ID de referencia
customer_id=ID de cliente
address_id=ID de dirección
order_id=ID de pedido
order_status_id=ID de estado del pedido
order_item_id=ID de detalle del pedido
carrier_id=ID de transportista
shipment_id=ID de envío
shipment_status_id=ID de estado del envío
promotion_type_id=ID de tipo de promoción
promotion_id=ID de promoción
payment_id=ID de pago
payment_method_id=ID de método de pago
payment_status_id=ID de estado del pago""".splitlines())

# These fields can be omitted; PostgreSQL still enforces the installed schema.
OPTIONAL = {"parent_category_id", "delivered_at", "shipped_at", "estimated_delivery_at"}
OPTIONAL_TEXT = {"description", "notes", "address_line2"}


def fields(repository, method):
    return [p for p in inspect.signature(getattr(repository, method)).parameters.values()
            if p.name != "self"]


def validate(parameters, raw):
    values = {}
    for field in parameters:
        name = field.name
        value = raw.get(name, "").strip()
        label = LABELS.get(name, name)
        if not value:
            if name in OPTIONAL:
                values[name] = None
                continue
            if name in OPTIONAL_TEXT:
                values[name] = ""
                continue
            raise ValueError(f"{label}: completa este campo.")
        try:
            if field.annotation is int:
                value = int(value)
                if (name.endswith("_id") and value <= 0) or (
                    name != "quantity" and value < 0
                ):
                    raise ValueError
            elif field.annotation is float:
                value = Decimal(value.replace(",", "."))
                if not value.is_finite() or value < 0:
                    raise ValueError
            elif name.endswith("_at"):
                value = datetime.fromisoformat(value)
            elif name == "email" and not re.fullmatch(r"[^\s@]+@[^\s@]+\.[^\s@]+", value):
                raise ValueError
            elif name == "currency_code":
                if not re.fullmatch(r"[A-Za-z]{3}", value):
                    raise ValueError
                value = value.upper()
        except (ValueError, InvalidOperation):
            raise ValueError(f"{label}: ingresa un valor válido.") from None
        values[name] = value
    if values.get("starts_at") and values.get("ends_at"):
        try:
            if values["ends_at"] < values["starts_at"]:
                raise ValueError("La fecha de fin debe ser posterior a la de inicio.")
        except TypeError:
            raise ValueError("Usa el mismo formato horario en ambas fechas.") from None
    return values
