from repo import ProductRepository


def main():
    """Run the main program flow for inserting a sample brand.

    This function creates a repository, inserts a sample brand, and closes
    the database connection afterward.
    """
    repo = ProductRepository()
    try:
        # repo.insert_brands(5, "NVIDIA")
        # print("Proceso finalizado")

        # repo.insert_product(2, "sfgdgg", "Manzana", "Red apple for you to eat")
        # print("Proceso finalizado")

        # repo.insert_category(1, "Shoes", "f1256", 1, "Shoes of all types to wear")
        # print("Proceso finalizado")

        # repo.insert_productcategories(1, 1)
        # print("Proceso finalizado")

        # repo.insert_productvarints(2, 1, "skdj13", "Banani", 3.5, 2.5, 2.5)
        # print("Proceso finalizado")

        repo.insert_product_attribute_keys(1, "f23l", "labl1")
        print("Proceso finalizado")
        
        repo.insert_variant_attribute_values (1, 1, 1, "Corazon")
        print("Proceso finalizado")
        
    finally:
        repo.close()


if __name__ == "__main__":
    main()
