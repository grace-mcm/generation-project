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

#Prints main menu options
def print_main_menu():
    print("-------------------------")
    print("MAIN MENU OPTIONS:")
    print("[1] - Products Menu")
    print("[2] - Orders Menu")
    print("[3] - Couriers Menu")
    print("[0] - Exit App")
    print("-------------------------")


#Takes user input and directs to relevant menu for further input
def main_menu():
    while True:
        print_main_menu()
        main_option = input("Please choose an option from the list:\n")

        if main_option == "1":
            from product_menu import products_menu
            products_menu()
        elif main_option == "2":
            from order_menu import order_menu
            order_menu()
        elif main_option == "3":
            from courier_menu import courier_menu
            courier_menu()
        elif main_option == "0":
            connection.commit()
            cursor.close()
            connection.close()
            exit()
            break
        else:
            print("Invalid option, please select 0-3 from main options:")

    
