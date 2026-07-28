from repo import ProductRepository


def main():
    repo = ProductRepository()
    try:
        repo.insert_product(1, "Adidas")
        print("Proceso finalizado")
    finally:
        repo.close()


if __name__ == "__main__":
    main()
