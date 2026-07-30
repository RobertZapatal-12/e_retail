from faker import Faker
import random
from datetime import datetime, timedelta


fake = Faker("es_ES")


NUM_ORDERS = 1000
NUM_ITEMS = 2500


def run_orders_seed(
    orders_repo,
):

    print("=== Iniciando Orders Seed ===")


    # =========================
    # ORDER STATUSES
    # =========================

    order_statuses = [
        ("PENDING", "Orden pendiente"),
        ("PROCESSING", "Orden en proceso"),
        ("SHIPPED", "Orden enviada"),
        ("DELIVERED", "Orden entregada"),
        ("CANCELLED", "Orden cancelada")
    ]


    for i, status in enumerate(order_statuses, start=1):

        orders_repo.insert_order_statuses(
            i,
            status[0],
            status[1]
        )


    # =========================
    # CARRIERS
    # =========================


    carriers = [
        "DHL",
        "FedEx",
        "UPS",
        "Caribe Express",
        "Metro Pac"
    ]


    for i, carrier in enumerate(carriers, start=1):

        orders_repo.insert_carriers(
            i,
            carrier,
            fake.phone_number()
        )



    # =========================
    # SHIPMENT STATUSES
    # =========================


    shipment_statuses = [
        ("READY", "Preparado"),
        ("IN_TRANSIT", "En tránsito"),
        ("DELIVERED", "Entregado"),
        ("FAILED", "Entrega fallida")
    ]


    for i, status in enumerate(shipment_statuses, start=1):

        orders_repo.insert_shipment_statuses(
            i,
            status[0],
            status[1]
        )



    # =========================
    # PROMOTION TYPES
    # =========================


    promotion_types = [
        ("PERCENTAGE", "Descuento por porcentaje"),
        ("FIXED", "Descuento fijo")
    ]


    for i, promo in enumerate(promotion_types, start=1):

        orders_repo.insert_promotion_types(
            i,
            promo[0],
            promo[1]
        )



    # =========================
    # PROMOTIONS
    # =========================


    promotions_ids = []


    for i in range(1, 21):

        orders_repo.insert_promotions(
            i,
            f"PROMO-{i}",
            f"Promoción {i}",
            fake.text(max_nb_chars=100),
            random.randint(1,2),
            random.randint(5,30),
            datetime.now(),
            datetime.now() + timedelta(days=30)
        )


        promotions_ids.append(i)



    # =========================
    # ORDERS
    # =========================


    orders_ids = []


    for i in range(1, NUM_ORDERS + 1):

        orders_repo.insert_orders(
            i,
            random.randint(1,1000),   # customers
            f"ORD-{10000+i}",
            random.randint(1,5),
            random.choice([
                "DOP",
                "USD"
            ])
        )


        orders_ids.append(i)




    # =========================
    # ORDER ITEMS
    # =========================


    for i in range(1, NUM_ITEMS + 1):

        quantity = random.randint(1,5)

        price = round(
            random.uniform(20,1500),
            2
        )


        orders_repo.insert_order_items(
            i,
            random.choice(orders_ids),
            random.randint(1,200),
            random.randint(1,400),
            random.randint(1,10),
            f"SKU-{random.randint(10000,99999)}",
            fake.word().title(),
            quantity,
            price,
            round(quantity * price,2),
            round(quantity * price * 0.18,2),
            round(random.uniform(0,50),2)
        )



    # =========================
    # SHIPMENTS
    # =========================


    for i in range(1, NUM_ORDERS + 1):

        orders_repo.insert_shipments(
            i,
            i,
            random.randint(1,5),
            fake.uuid4()[:15],
            datetime.now(),
            datetime.now() + timedelta(days=5),
            None,
            random.randint(1,4),
            round(random.uniform(100,500),2)
        )



    # =========================
    # ORDER PROMOTIONS
    # =========================


    for order_id in orders_ids:

        if random.choice([True,False]):

            orders_repo.insert_order_promotions(
                order_id,
                random.choice(promotions_ids),
                round(random.uniform(5,100),2)
            )



    print("=== Orders Seed completado ===")