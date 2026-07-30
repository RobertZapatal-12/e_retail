from faker import Faker
import random


fake = Faker("es_ES")


def run_payments_seed(payments_repo):

    print("=== Iniciando Payments Catalogs Seed ===")

    currencies = [
        ("DOP", "Peso Dominicano"),
        ("USD", "Dólar Estadounidense"),
        ("EUR", "Euro")
    ]

    for code, name in currencies:
        payments_repo.insert_currencies(
            code,
            name
        )


    payment_methods = [
        ("CREDIT_CARD", "Tarjeta de crédito"),
        ("DEBIT_CARD", "Tarjeta de débito"),
        ("PAYPAL", "PayPal"),
        ("BANK_TRANSFER", "Transferencia bancaria"),
        ("CASH", "Efectivo")
    ]


    for i, method in enumerate(payment_methods, start=1):
        payments_repo.insert_payment_methods(
            i,
            method[0],
            method[1]
        )


    payment_statuses = [
        ("PENDING", "Pendiente"),
        ("COMPLETED", "Completado"),
        ("FAILED", "Fallido"),
        ("REFUNDED", "Reembolsado")
    ]


    for i, status in enumerate(payment_statuses, start=1):
        payments_repo.insert_payment_statuses(
            i,
            status[0],
            status[1]
        )


    print("=== Catálogos Payments completados ===")



def run_payments_data_seed(payments_repo):

    print("=== Insertando Payments ===")


    NUM_PAYMENTS = 1000


    for i in range(1, NUM_PAYMENTS + 1):

        payments_repo.insert_payments(
            i,
            i,  # order_id
            random.randint(1,5),
            random.randint(1,4),
            random.choice([
                "Stripe",
                "PayPal",
                "Visa",
                "Mastercard"
            ]),
            round(random.uniform(50,3000),2),
            random.choice([
                "DOP",
                "USD"
            ]),
            fake.uuid4()
        )


    print("=== Payments insertados ===")
