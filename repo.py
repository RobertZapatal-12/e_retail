from database import get_connection
import datetime as datetime


class ProductRepository:
    """Repository class for managing brand data in PostgreSQL."""

    def __init__(self, conn=None):
        """Initialize the repository with a database connection.

        Args:
            conn: An existing database connection. If None, a new one is created.
        """
        self.conn = conn or get_connection()

    def insert_brands(self, brand_id: int, name: str):
        """Insert a new brand into the database.

        Args:
            brand_id: The identifier of the brand.
            name: The brand name to insert.
        """
        with self.conn.cursor() as cur:
            cur.execute(
                "INSERT INTO public.brands (brand_id, name) VALUES (%s, %s)",
                (brand_id, name),
            )
            self.conn.commit()
            print("Insertado correctamente")

    def close(self):
        """Close the database connection if it exists."""
        if self.conn is not None:
            self.conn.close()

    def get_version(self):
        """Return the PostgreSQL server version.

        Returns:
            tuple: A tuple containing the database version information.
        """
        with self.conn.cursor() as cur:
            cur.execute("SELECT version()")
            return cur.fetchone()

    def insert_product(
        self,
        product_id: int,
        sku: str,
        name: str,
        description: str,
    ):
        """Insert a new product into the database.

        Args:
            product_id: The identifier of the product.
            sku: The product SKU.
            name: The product name.
            description: The product description.
        """
        with self.conn.cursor() as cur:
            cur.execute("INSERT INTO products (product_id, sku, name, description) VALUES (%s, %s, %s, %s)",
                        (product_id, sku, name, description))
            self.conn.commit()
            print("Insertado correctamente")

    def insert_category(
        self,
        category_id: int,
        name: str,
        slug: str,
        parent_category_id: int,
        description: str,
    ):
        """Insert a new category into the database.

        Args:
            category_id: The identifier of the category.
            name: The category name.
            slug: The category slug.
            parent_category_id: The parent category identifier, if any.
            description: The category description.
        """
        with self.conn.cursor() as cur:
            cur.execute("INSERT INTO categories (category_id, name, slug, parent_category_id, description) VALUES (%s, %s, %s, %s, %s)",
                        (category_id, name, slug, parent_category_id, description))
            self.conn.commit()
            print("Insertado correctamente")

    def insert_productcategories(
        self, 
        product_id : int, 
        category_id : int
    ):
        """Insert a relationship between a product and a category.

        Args:
            product_id: The identifier of the product.
            category_id: The identifier of the category.
        """
        with self.conn.cursor() as cur:
            cur.execute("INSERT INTO product_categories (product_id, category_id) VALUES (%s, %s)",
                        (product_id, category_id))
            self.conn.commit()
            print("Insertado correctamente")

    def insert_productvarints(
        self,
        variant_id : int,
        product_id : int,
        sku : str,
        name : str,
        price : float,
        cost_price : float,
        weight_kg : float
    ):
        """Insert a product variant with its pricing and weight data.

        Args:
            variant_id: The identifier of the variant.
            product_id: The identifier of the parent product.
            sku: The SKU of the variant.
            name: The name of the variant.
            price: The selling price.
            cost_price: The cost price.
            weight_kg: The weight in kilograms.
        """
        with self.conn.cursor() as cur:
            cur.execute("INSERT INTO product_variants (variant_id, product_id, sku, name, price, cost_price, weight_kg) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                        (variant_id, product_id, sku, name, price, cost_price, weight_kg))

            self.conn.commit()
            print("Insertado correctamente")

    def insert_product_attribute_keys(
            self, 
            attribute_key_id : int, 
            code : str,
            label : str
        ):
            """Insert an attribute key used by products.

            Args:
                attribute_key_id: The identifier of the attribute key.
                code: The attribute code.
                label: The human-readable label.
            """
            with self.conn.cursor() as cur:
                cur.execute("INSERT INTO product_attribute_keys (attribute_key_id, code, label) VALUES (%s, %s, %s)",
                            (attribute_key_id, code, label))
                self.conn.commit()
                print("Insertado correctamente")

    def insert_variant_attribute_values(
        self,
        variant_attribute_value_id : int,  
        variant_id : int,
        attribute_key_id : int,     
        value : str
    ):
        """Insert the value of an attribute for a specific variant.

        Args:
            variant_attribute_value_id: The identifier of the value record.
            variant_id: The identifier of the variant.
            attribute_key_id: The identifier of the attribute key.
            value: The attribute value.
        """
        with self.conn.cursor() as cur:
            cur.execute("INSERT INTO variant_attribute_values (variant_attribute_value_id, variant_id, attribute_key_id, value) VALUES (%s, %s, %s, %s)",
                        (variant_attribute_value_id, variant_id, attribute_key_id, value))
        self.conn.commit()
        print("Insertado correctamente")