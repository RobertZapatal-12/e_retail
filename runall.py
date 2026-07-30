from database import get_connection

from product_repo import ProductRepository
from customers_repo import CustomersRepository
from payments_repo import PaymentsRepository
from orders_repo import OrdersRepository


from products_seed import run_products_seed
from customers_seed import run_customers_seed
from payments_seed import run_payments_seed, run_payments_data_seed
from orders_seed import run_orders_seed



def run_all():

    print("==============================")
    print(" INICIANDO SEED DATABASE ")
    print("==============================")


    conn = get_connection()


    try:

        products_repo = ProductRepository(conn)
        customers_repo = CustomersRepository(conn)
        payments_repo = PaymentsRepository(conn)
        orders_repo = OrdersRepository(conn)


        # -------------------------
        # PRODUCTS
        # -------------------------

        print("\n[1] Productos")
        run_products_seed(products_repo)



        # -------------------------
        # CUSTOMERS
        # -------------------------

        print("\n[2] Clientes")
        run_customers_seed(customers_repo)



        # -------------------------
        # PAYMENTS CATALOGS
        # -------------------------

        print("\n[3] Catálogos de pagos")
        run_payments_seed(payments_repo)



        # -------------------------
        # ORDERS
        # -------------------------

        print("\n[4] Ordenes")
        run_orders_seed(orders_repo)



        # -------------------------
        # PAYMENTS
        # -------------------------

        print("\n[5] Pagos")
        run_payments_data_seed(payments_repo)



        print("\n==============================")
        print(" SEED COMPLETADO ")
        print("==============================")


    except Exception as e:

        print("\nERROR:")
        print(e)

        conn.rollback()


    finally:

        conn.close()