from product_repo import ProductRepository
from payments_repo import PaymentsRepository


def main():
    """Run the main program flow for inserting a sample brand.

    This function creates a repository, inserts a sample brand, and closes
    the database connection afterward.
    """
    # repo = ProductRepository()
    # try:
    #     # repo.insert_brands(5, "NVIDIA")
    #     # print("Proceso finalizado")

    #     # repo.insert_product(2, "sfgdgg", "Manzana", "Red apple for you to eat")
    #     # print("Proceso finalizado")

    #     # repo.insert_category(1, "Shoes", "f1256", 1, "Shoes of all types to wear")
    #     # print("Proceso finalizado")

    #     # repo.insert_productcategories(1, 1)
    #     # print("Proceso finalizado")

    #     # repo.insert_productvarints(2, 1, "skdj13", "Banani", 3.5, 2.5, 2.5)
    #     # print("Proceso finalizado")

    #     # repo.insert_product_attribute_keys(1, "f23l", "labl1")
    #     # print("Proceso finalizado")

    #     # repo.insert_variant_attribute_values (1, 1, 1, "Corazon")
    #     # print("Proceso finalizado")

    #     # repo.insert_suppliers(1, "Claro", "Robert Yarel", "yarelzapatal@gmail.com", "8098632010", "Santo Domingo Este")
    #     # print("Proceso finalizado")

    #     # repo.insert_product_suppliers(1, 1, "12skgj", 7)
    #     # print("Proceso finalizado")
        
    #     # repo.insert_stores(1, "Apple", "Time Squares", "la tablita", "tal", "Santo Domingo", "1452", "Alma rosa", "Republica Dominicana", "8097656666")
    #     # print("Proceso finalizado")

    #     # repo.insert_inventory(1, 1, 1, 1, 12, 45, 11)
    #     # print("Proceso finalizado")

    #     # repo.insert_inventory_transactions(1, 1, "card", 45, "y tal", 1, "This is some bread. You have to know that its about time to eat, so enjoy.")
    #     # print("Proceso finalizado")

    # finally:
    #     repo.close()

    pay_repo = PaymentsRepository()
    try:
        pay_repo.insert_payment_methods(1, "sd21", "He is paying with card")
        print("Proceso finalizado")

    finally:
        pay_repo.close()


if __name__ == "__main__":
    main()
