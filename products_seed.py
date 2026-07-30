from faker import Faker
import random
import re
import unicodedata


fake = Faker("es_ES")


# Cantidad de datos
NUM_BRANDS = 20
NUM_CATEGORIES = 30
NUM_PRODUCTS = 200
NUM_VARIANTS = 400
NUM_SUPPLIERS = 30
NUM_STORES = 10



def create_slug(text, used_slugs):

    text = unicodedata.normalize(
        "NFD",
        text
    ).encode(
        "ascii",
        "ignore"
    ).decode(
        "utf-8"
    )

    slug = re.sub(
        r"[^a-zA-Z0-9]+",
        "-",
        text.lower()
    ).strip("-")


    original_slug = slug
    counter = 1


    while slug in used_slugs:
        slug = f"{original_slug}-{counter}"
        counter += 1


    used_slugs.add(slug)

    return slug



def unique_value(value, used_values):

    original = value
    counter = 1


    while value in used_values:
        value = f"{original}-{counter}"
        counter += 1


    used_values.add(value)

    return value





def run_products_seed(products_repo):

    print("=== Iniciando Products Seed ===")



    # =========================
    # BRANDS
    # =========================

    brands_ids = []

    used_brands = set()


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

        name = (
            brands[i-1]
            if i <= len(brands)
            else fake.company()
        )


        name = unique_value(
            name,
            used_brands
        )


        products_repo.insert_brands(
            i,
            name
        )


        brands_ids.append(i)




    # =========================
    # CATEGORIES
    # =========================

    categories_ids = []

    used_category_slugs = set()


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

        name = (
            categories[i-1]
            if i <= len(categories)
            else fake.word().title()
        )


        slug = create_slug(
            name,
            used_category_slugs
        )


        products_repo.insert_category(
            i,
            name,
            slug,
            None,
            fake.text(max_nb_chars=100)
        )


        categories_ids.append(i)




    # =========================
    # PRODUCTS
    # =========================

    products_ids = []


    for i in range(1, NUM_PRODUCTS + 1):

        brand_id = random.choice(brands_ids)


        products_repo.insert_product(
            brand_id,
            i,
            f"SKU-{10000+i}",
            fake.catch_phrase(),
            fake.text(max_nb_chars=200)
        )


        products_ids.append(i)




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


    variant_names = [
        "Base",
        "Pro",
        "Gaming",
        "Ultra",
        "Plus"
    ]


    for i in range(1, NUM_VARIANTS + 1):

        product_id = random.choice(products_ids)


        products_repo.insert_productvarints(
            i,
            product_id,
            f"VAR-{10000+i}",
            random.choice(variant_names),
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

    used_emails = set()


    for i in range(1, NUM_SUPPLIERS + 1):

        email = fake.unique.email()


        products_repo.insert_suppliers(
            i,
            fake.company(),
            fake.name(),
            email,
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