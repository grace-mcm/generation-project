from product_db_utils import (get_product, update_product_name, update_product_price, delete_product_record, product_list, add_new_product)
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

#Prints product menu options
def print_products_menu():
    print("-------------------------")
    print("PRODUCT MENU OPTIONS:")
    print("[1] - Print Products List")
    print("[2] - Add a Product")
    print("[3] - Update a Product")
    print("[4] - Remove a Product")
    print("[0] - Back to Main Menu")
    print("-------------------------")

def products_menu():
    while True:
        print_products_menu()

#executes functions to allow user to edit data stored in products dictionary

        product_option = input("Please select an option:\n")

        if product_option == '1':#prints current product menu
            product_list()
        elif product_option == '2':#allows a user to add a product to a list
            add_product()   
        elif product_option == '3':#allows a user to select a product on the list and update it
            update_product()   
        elif product_option == '4':#allows a user to select a product on the list and delete it
            remove_product()
        elif product_option == '0': #takes the user back to the main menu
            from main_menu import main_menu
            main_menu() 
            break 
        else:
            print("Invalid option, please select 0-4 from product options:")


#allows user to add a new product to the product list
def add_product():
    product_name = input("Please enter new product name:")
    product_price = input("Please enter new product price:")
    add_new_product(product_name, product_price)
    print("Here is the updated product list:")
    product_list()

#allows user to update the name and/or price of an existing product
def update_product():
    product_list()
    try:
        query_update_product = int(input("Please select the product ID you would like to update:\n"))
        #get_product(query_update_product)
        if input("Would you like to update the product name (y/n)?\n").lower() == "y":
            new_product_name = input("Please enter new name for product:\n")
            update_product_name(new_product_name, query_update_product)

        if input("Would you like to update product price (y/n)?\n").lower() == "y":
            new_product_price = float(input("Please enter new price for product:\n"))
            update_product_price(new_product_price, query_update_product)
        
        print("Here is the updated product list:")
        product_list()
    except: 
        print("Invalid input!")

def remove_product():
    product_list()
    try:
        query_remove_product = int(input("Please select the product ID you would like to remove:"))
        #get_product(query_remove_product)
        delete_product_record(query_remove_product)
        print("Here is the updated product list:")
        product_list()
    except:
        print("Invalid input!")
