from faker import Faker
import random


fake = Faker("es_ES")


NUM_CUSTOMERS = 1000
NUM_ADDRESSES = 1500


def run_customers_seed(customers_repo):

    print("=== Iniciando Customers Seed ===")


    # =========================
    # CUSTOMERS
    # =========================

    customers_ids = []


    for i in range(1, NUM_CUSTOMERS + 1):

        first_name = fake.first_name()
        last_name = fake.last_name()


        customers_repo.insert_customers(
            i,
            first_name,
            last_name,
            f"{first_name.lower()}.{last_name.lower()}{i}@gmail.com",
            fake.phone_number()
        )


        customers_ids.append(i)



    # =========================
    # CUSTOMER ADDRESSES
    # =========================


    for i in range(1, NUM_ADDRESSES + 1):

        customer_id = random.choice(customers_ids)


        customers_repo.insert_customer_addresses(
            i,
            customer_id,
            fake.street_address(),
            fake.secondary_address(),
            fake.city(),
            fake.state(),
            fake.postcode(),
            "República Dominicana"
        )



    print("=== Customers Seed completado ===")