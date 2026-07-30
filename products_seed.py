from faker import Faker
import random


fake = Faker("es_ES")


# Cantidad de datos
NUM_BRANDS = 20
NUM_CATEGORIES = 30
NUM_PRODUCTS = 200
NUM_VARIANTS = 400
NUM_SUPPLIERS = 30
NUM_STORES = 10


def run_products_seed(products_repo):

    print("=== Iniciando Products Seed ===")


    # =========================
    # BRANDS
    # =========================

    brands_ids = []

    brands = [
        "Apple",
        "Samsung",
        "Lenovo",
        "Dell",
        "HP",
        "Logitech",
        "Sony",
        "Asus",
        "Acer",
        "Microsoft"
    ]

    for i in range(1, NUM_BRANDS + 1):

        name = brands[i-1] if i <= len(brands) else fake.company()

        products_repo.insert_brands(
            i,
            name
        )

        brands_ids.append(i)


    # =========================
    # CATEGORIES
    # =========================

    categories_ids = []

    categories = [
        "Laptops",
        "Smartphones",
        "Monitores",
        "Teclados",
        "Mouse",
        "Audífonos",
        "Componentes PC",
        "Gaming",
        "Accesorios",
        "Tablets"
    ]


    for i in range(1, NUM_CATEGORIES + 1):

        name = categories[i-1] if i <= len(categories) else fake.word().title()

        products_repo.insert_category(
            i,
            name,
            name.lower().replace(" ", "-"),
            None,
            fake.text(max_nb_chars=100)
        )

        categories_ids.append(i)



    # =========================
    # PRODUCTS
    # =========================

    products_ids = []


    for i in range(1, NUM_PRODUCTS + 1):

        product_id = i

        products_repo.insert_product(
            product_id,
            f"SKU-{10000+i}",
            fake.catch_phrase(),
            fake.text(max_nb_chars=200)
        )

        products_ids.append(product_id)



    # =========================
    # PRODUCT CATEGORIES
    # =========================


    for product_id in products_ids:

        category_id = random.choice(categories_ids)

        products_repo.insert_productcategories(
            product_id,
            category_id
        )



    # =========================
    # ATTRIBUTE KEYS
    # =========================


    attributes = [
        ("COLOR", "Color"),
        ("SIZE", "Tamaño"),
        ("MEMORY", "Memoria RAM"),
        ("STORAGE", "Almacenamiento"),
        ("MODEL", "Modelo")
    ]


    attribute_ids = []


    for i, attribute in enumerate(attributes, start=1):

        products_repo.insert_product_attribute_keys(
            i,
            attribute[0],
            attribute[1]
        )

        attribute_ids.append(i)




    # =========================
    # PRODUCT VARIANTS
    # =========================


    variants_ids = []


    for i in range(1, NUM_VARIANTS + 1):

        product_id = random.choice(products_ids)


        products_repo.insert_productvarints(
            i,
            product_id,
            f"VAR-{10000+i}",
            fake.word().title(),
            round(random.uniform(20,2000),2),
            round(random.uniform(10,1500),2),
            round(random.uniform(0.1,5),2)
        )

        variants_ids.append(i)




    # =========================
    # VARIANT ATTRIBUTES
    # =========================


    colors = [
        "Negro",
        "Blanco",
        "Rojo",
        "Azul",
        "Gris"
    ]


    for i, variant_id in enumerate(variants_ids, start=1):

        attribute_id = random.choice(attribute_ids)


        products_repo.insert_variant_attribute_values(
            i,
            variant_id,
            attribute_id,
            random.choice(colors)
        )




    # =========================
    # SUPPLIERS
    # =========================


    suppliers_ids = []


    for i in range(1, NUM_SUPPLIERS + 1):

        products_repo.insert_suppliers(
            i,
            fake.company(),
            fake.name(),
            fake.email(),
            fake.phone_number(),
            fake.address()
        )

        suppliers_ids.append(i)




    # =========================
    # PRODUCT SUPPLIERS
    # =========================


    for product_id in products_ids:

        supplier_id = random.choice(suppliers_ids)


        products_repo.insert_product_suppliers(
            product_id,
            supplier_id,
            f"SUP-{product_id}",
            random.randint(1,30)
        )




    # =========================
    # STORES
    # =========================


    stores_ids = []


    for i in range(1, NUM_STORES + 1):

        products_repo.insert_stores(
            i,
            f"Tienda {i}",
            fake.city(),
            fake.street_address(),
            "",
            fake.city(),
            fake.state(),
            fake.postcode(),
            "República Dominicana",
            fake.phone_number()
        )


        stores_ids.append(i)




    # =========================
    # INVENTORY
    # =========================


    inventory_ids = []


    for i in range(1, NUM_PRODUCTS + 1):

        product_id = random.choice(products_ids)
        variant_id = random.choice(variants_ids)
        store_id = random.choice(stores_ids)


        products_repo.insert_inventory(
            i,
            product_id,
            variant_id,
            store_id,
            random.randint(10,500),
            random.randint(0,20),
            random.randint(5,50)
        )

        inventory_ids.append(i)




    # =========================
    # INVENTORY TRANSACTIONS
    # =========================


    for i, inventory_id in enumerate(inventory_ids, start=1):

        products_repo.insert_inventory_transactions(
            i,
            inventory_id,
            random.choice([
                "IN",
                "OUT"
            ]),
            random.randint(1,100),
            random.choice([
                "Compra proveedor",
                "Venta cliente"
            ]),
            random.randint(1,10000),
            fake.sentence()
        )



    print("=== Products Seed completado ===")