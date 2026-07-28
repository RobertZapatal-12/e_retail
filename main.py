from repo import ProductRepository


def main():
    """Run the main program flow for inserting a sample brand.

    This function creates a repository, inserts a sample brand, and closes
    the database connection afterward.
    """
    repo = ProductRepository()
    try:
        repo.insert_product(1, "Adidas")
        print("Proceso finalizado")
    finally:
        repo.close()


if __name__ == "__main__":
    main()
