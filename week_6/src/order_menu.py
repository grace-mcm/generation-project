from order_db_utils import(customer_list, status_list, order_list, orderline_list, update_order_courier, update_order_status, update_order_customer, delete_order_record, get_order, get_orderline, view_orderline, add_new_order, add_new_orderline, add_new_customer)
from courier_db_utils import(courier_list)
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

#Prints the main options for the Order Menu and navigates based on user input
def print_order_menu():
    print("-------------------------")
    print("ORDER MENU OPTIONS:")
    print("[1] - Print Orders List")
    print("[2] - Add an Order")
    print("[3] - Update an Order")
    print("[4] - Remove an Order")
    print("[0] - Back to Main Menu")
    print("-------------------------")

def order_menu():
    while True:
        print_order_menu()
        order_option = input("Please select an option:\n")

        if order_option == '1':#prints current product menu
            order_list()
            view_orderline()
        elif order_option == '2':#allows a user to add a product to a list
            add_order()  
        elif order_option == '3':#allows a user to select a product on the list and update it
            update_order()  
        elif order_option == '4':#allows a user to select a product on the list and delete it
            remove_order()
        elif order_option == "0":#takes user back to the main menu options
            from main_menu import main_menu
            main_menu()
            break 
        else:
            print("Invalid option, please select 0-4 from product options:")


#Takes user through the process of adding a new order record to the table
def add_order():
    query_new_customer()
    customer_list()
    customer = input("Please select the customer ID:\n")
    courier_list()
    courier = input("Please select courier ID:\n")
    status_list()
    status = input("Please select status ID:\n")
    add_new_order(customer, courier, status)
    order_list()
    query_order_id = int(input("Please confirm order ID you would like to add items to:\n"))
    add_orderline(query_order_id)
    

#Allows user to add each item from a customer order and matches it to the order ID from the parent order table
def add_orderline(order_id):
    while True:
        query_add_items = input("Would you like to add an item to the order (y/n):\n").lower()
        if query_add_items == "y":
            order_list()
            item = input("Please enter ID of product you would like to add to order:\n")
            add_new_orderline(order_id, item)
        elif query_add_items == "n":
            break
        else:
            print("Invalid option! Please select 'y' to add another item or 'n' to finish adding items:\n")


#asks if the user would like to add an order to existing customer or create a new one
def query_new_customer():
    print("Here is the current customer list:\n")
    customer_list()

    while True:
        is_customer = input("Select 'e' to add order for an existing customer or 'n' to add a new customer:\n").lower()
        if is_customer == "n":
            add_customer()
        elif is_customer == "e":
            break
        else:
            print("Invalid option! Please enter 'e' for an existing customer or 'n' to add a new customer:\n")

#Allows user to add a new customer to the customer table
def add_customer():
    customer_name = input("Please enter the customer name:\n")
    customer_address = input("Please enter customer address:\n")
    customer_phone = input("Please enter customer phone number:\n")
    add_new_customer(customer_name, customer_address, customer_phone)

#Takes the user through the process of updating an existing order record
def update_order():
    order_list()
    try:
        query_order = input("Please select the order ID you would like to update:\n")
        get_order(query_order)

        if input("Would you like to update the customer (y/n)?\n").lower() == "y":
            customer_list()
            customer = input("Please select the customer ID:\n")
            update_order_customer(customer, query_order)

        if input("Would you like to update the courier (y/n)?\n").lower() == "y":
            courier_list()
            courier = input("Please select courier ID:\n")
            update_order_courier(courier, query_order)

        if input("Would you like to update the order status (y/n)? \n").lower() == "y":
            status_list()
            status = input("Pleae select status ID:\n")
            update_order_status(status, query_order)
        
        if input("Would you like to update the order items (y/n)? \n").lower() == "y":
            add_orderline(query_order)

    except:
        print("Invalid input!")


#Executes functions to select and remove an order record based on user input
def remove_order():
    order_list()
    try:
        query_order = input("Please select the order you would like to remove:\n")
        get_order(query_order)
        delete_order_record(query_order)
        connection.commit()
        print("Here is the updated orders list:")
        order_list()
    except: 
        print("Invaild option!")