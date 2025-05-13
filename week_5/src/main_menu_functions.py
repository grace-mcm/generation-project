from product_menu_functions import *
from courier_menu_functions import *
from order_menu_functions import *
import psycopg2
import os
from dotenv import load_dotenv
load_dotenv()
host_name = os.environ.get("POSTGRES_HOST")
database_name = os.environ.get("POSTGRES_DB")
user_name = os.environ.get("POSTGRES_USER")
user_password = os.environ.get("POSTGRES_PASSWORD")
connection = psycopg2.connect(f"""
    host={host_name}
    dbname={database_name}
    user={user_name}
    password={user_password}
    """)

cursor = connection.cursor()
def print_main_menu():
    print("-------------------------")
    print("MAIN MENU OPTIONS:")
    print("[1] - Products Menu")
    print("[2] - Orders Menu")
    print("[3] - Couriers Menu")
    print("[0] - Exit App")
    print("-------------------------")

    
def main_menu(main_option):
    print_main_menu()
    print("Please choose an option from the main menu:\n")
    try:
        if main_option == '1':
            return products_menu()
        elif main_option == '2':
            return order_menu()
        elif main_option == '3':
            return courier_menu()
        elif main_option == '0':
            cursor.close()
            connection.close()
            return exit()
        else:
                print("Invalid option, please select 0-3 from main options:")
                main_menu()
    except:
        print("Invalid option, please select 0-3 from main options:")
        main_menu()

