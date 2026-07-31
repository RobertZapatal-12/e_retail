from database import get_connection
import datetime as datetime


class OrdersRepository:
    def __init__(self, conn=None):
        self.conn = conn or get_connection()

    def close(self):
        """Close the database connection if it exists."""
        if self.conn is not None:
            self.conn.close()

    def insert_order_statuses(self, order_status_id: int, code: str, description: str):
        with self.conn.cursor() as cur:
            cur.execute(
                "INSERT INTO order_statuses (order_status_id, code, description) VALUES (%s, %s, %s)",
                (order_status_id, code, description),
            )
            self.conn.commit()
            print("Insertado correctamente")

    def insert_orders(
        self,
        order_id: int,
        customer_id: int,
        order_number: str,
        order_status_id: int,
        currency_code: str,
    ):
        with self.conn.cursor() as cur:
            cur.execute(
                "INSERT INTO orders (order_id, customer_id, order_number, order_status_id, currency_code) VALUES (%s, %s, %s, %s, %s)",
                (order_id, customer_id, order_number, order_status_id, currency_code),
            )
            self.conn.commit()
            print("Insertado correctamente")

    def insert_order_items(
        self,
        order_item_id: int,
        order_id: int,
        product_id: int,
        variant_id: int,
        store_id: int,
        sku: str,
        name: str,
        quantity: int,
        unit_price: float,
        line_total: float,
        tax_amount: float,
        discount_amount: float,
    ):
        with self.conn.cursor() as cur:
            cur.execute(
                "INSERT INTO order_items (order_item_id, order_id, product_id, variant_id, store_id, sku, name, quantity, unit_price, line_total, tax_amount, discount_amount) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                (
                    order_item_id,
                    order_id,
                    product_id,
                    variant_id,
                    store_id,
                    sku,
                    name,
                    quantity,
                    unit_price,
                    line_total,
                    tax_amount,
                    discount_amount,
                ),
            )
            self.conn.commit()
            print("Insertado correctamente")

    def insert_carriers(self, carrier_id: int, name: str, contact_info: str):
        with self.conn.cursor() as cur:
            cur.execute(
                "INSERT INTO carriers (carrier_id, name, contact_info) VALUES (%s, %s, %s)",
                (carrier_id, name, contact_info),
            )
            self.conn.commit()
            print("Insertado correctamente")

    def insert_shipment_statuses(
        self, shipment_status_id: int, code: str, description: str
    ):
        with self.conn.cursor() as cur:
            cur.execute(
                "INSERT INTO shipment_statuses (shipment_status_id, code, description) VALUES (%s, %s, %s)",
                (shipment_status_id, code, description),
            )
            self.conn.commit()
            print("Insertado correctamente")

    def insert_shipments(
        self,
        shipment_id: int,
        order_id: int,
        carrier_id: int,
        tracking_number: str,
        shipped_at: str,
        estimated_delivery_at: str,
        delivered_at: str,
        shipment_status_id: int,
        shipping_amount: float,
    ):
        with self.conn.cursor() as cur:
            cur.execute(
                "INSERT INTO shipments (shipment_id, order_id, carrier_id, tracking_number, shipped_at, estimated_delivery_at, delivered_at, shipment_status_id, shipping_amount) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
                (
                    shipment_id,
                    order_id,
                    carrier_id,
                    tracking_number,
                    shipped_at,
                    estimated_delivery_at,
                    delivered_at,
                    shipment_status_id,
                    shipping_amount,
                ),
            )
            self.conn.commit()
            print("Insertado correctamente")

    def insert_promotion_types(
        self, promotion_type_id: int, code: str, description: str
    ):
        with self.conn.cursor() as cur:
            cur.execute(
                "INSERT INTO promotion_types (promotion_type_id, code, description) VALUES (%s, %s, %s)",
                (promotion_type_id, code, description),
            )
            self.conn.commit()
            print("Insertado correctamente")

    def insert_promotions(
        self,
        promotion_id: int,
        code: str,
        name: str,
        description: str,
        promotion_type_id: int,
        value: float,
        starts_at: str,
        ends_at: str,
    ):
        with self.conn.cursor() as cur:
            cur.execute(
                "INSERT INTO promotions (promotion_id, code, name, description, promotion_type_id, value, starts_at, ends_at) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                (
                    promotion_id,
                    code,
                    name,
                    description,
                    promotion_type_id,
                    value,
                    starts_at,
                    ends_at,
                ),
            )
            self.conn.commit()
            print("Insertado correctamente")

    def insert_order_promotions(
        self, order_id: int, promotion_id: int, discount_amount: float
    ):
        with self.conn.cursor() as cur:
            cur.execute(
                "INSERT INTO order_promotions (order_id, promotion_id, discount_amount) VALUES (%s, %s, %s)",
                (order_id, promotion_id, discount_amount),
            )
            self.conn.commit()
            print("Insertado correctamente")
