from product_repo import ProductRepository
from payments_repo import PaymentsRepository
from orders_repo import OrdersRepository
from customers_repo import CustomersRepository


def main():
    """Run the main program flow for inserting a sample brand.

    This function creates a repository, inserts a sample brand, and closes
    the database connection afterward.
    """
    repo = ProductRepository()
    try:
        repo.insert_brands(5, "NVIDIA")
        print("Proceso finalizado")

        repo.insert_product(2, "sfgdgg", "Manzana", "Red apple for you to eat")
        print("Proceso finalizado")

        repo.insert_category(1, "Shoes", "f1256", 1, "Shoes of all types to wear")
        print("Proceso finalizado")

        repo.insert_productcategories(1, 1)
        print("Proceso finalizado")

        repo.insert_productvarints(2, 1, "skdj13", "Banani", 3.5, 2.5, 2.5)
        print("Proceso finalizado")

        repo.insert_product_attribute_keys(1, "f23l", "labl1")
        print("Proceso finalizado")

        repo.insert_variant_attribute_values (1, 1, 1, "Corazon")
        print("Proceso finalizado")

        repo.insert_suppliers(1, "Claro", "Robert Yarel", "yarelzapatal@gmail.com", "8098632010", "Santo Domingo Este")
        print("Proceso finalizado")

        repo.insert_product_suppliers(1, 1, "12skgj", 7)
        print("Proceso finalizado")
        
        repo.insert_stores(1, "Apple", "Time Squares", "la tablita", "tal", "Santo Domingo", "1452", "Alma rosa", "Republica Dominicana", "8097656666")
        print("Proceso finalizado")

        repo.insert_inventory(1, 1, 1, 1, 12, 45, 11)
        print("Proceso finalizado")

        repo.insert_inventory_transactions(1, 1, "card", 45, "y tal", 1, "This is some bread. You have to know that its about time to eat, so enjoy.")
        print("Proceso finalizado")

    finally:
        repo.close()

    pay_repo = PaymentsRepository()
    try:
        pay_repo.insert_payment_methods(1, "sd21", "He is paying with card")
        print("Proceso finalizado")

        pay_repo.insert_payment_statuses(1, "sf1231", "Is a good status")
        print("Proceso finalizado")

        pay_repo.insert_payments(1, 1, 1, 1, "Tele Group", 12.5, "a1", "DDFYRHJSKA1234")
        print("Proceso finalizado")

        pay_repo.insert_currencies("a1", "Euro")
        print("Proceso finalizado")
        


    finally:
        pay_repo.close()
      
    orders_repo = OrdersRepository()
    try:
        orders_repo.insert_order_statuses(1, "ADD12", "Good")
        print("Proceso finalizado")

        orders_repo.insert_orders(1, 1, "123", 1, "a1")
        print("Proceso finalizado")

        orders_repo.insert_order_items(1, 1, 1, 1, 1, "SKU-001", "Laptop Lenovo", 2, 450.00, 900.00, 162.00, 50.00)
        print("Proceso finalizado")

        orders_repo.insert_carriers(1, "DHL", "809-555-1234")
        print("Proceso finalizado")

        orders_repo.insert_shipment_statuses(1, "SHIPPED", "Enviado al cliente")
        print("Proceso finalizado")

        orders_repo.insert_shipments(1, 1, 1, "TRK123456789", "2026-07-30 10:00:00", "2026-08-02 18:00:00", None, 1, 250.00)
        print("Proceso finalizado")

        orders_repo.insert_promotion_types(1, "PERCENTAGE", "Descuento porcentual")
        print("Proceso finalizado")

        orders_repo.insert_promotions(1, "PROMO10", "Descuento de bienvenida", "10 por ciento de descuento en la primera compra", 1, 10.00, "2026-07-01 00:00:00", "2026-12-31 23:59:59")
        print("Proceso finalizado")

        orders_repo.insert_order_promotions(1, 1, 90.00)
        print("Proceso finalizado")


    finally:
        orders_repo.close()

    cust_repo = CustomersRepository()
    try:
        cust_repo.insert_customers(1, "Robert Yarel", "Zapata Linares", "yarelzapatal@gmail.com", "8097657654")
        print("Proceso finalizado")

        cust_repo.insert_customer_addresses(1, 1, "Calle Duarte #123", "Apto. 2B", "Santo Domingo", "Distrito Nacional", "10101", "República Dominicana")
        print("Proceso finalizado")

    finally:
        cust_repo.close


if __name__ == "__main__":
    main()
