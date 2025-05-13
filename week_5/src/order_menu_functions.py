from main_menu_functions import *
from courier_menu_functions import *
from product_menu_functions import *
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
def order_menu():
    print("-------------------------")
    print("ORDER MENU OPTIONS:")
    print("[1] - Print Orders List")
    print("[2] - Add an Order")
    print("[3] - Update an Order")
    print("[4] - Remove an Order")
    print("[0] - Back to Main Menu")
    print("-------------------------")

    order_option = input("Please select an option:\n")
    try:
        if order_option == '1':#prints current product menu
            order_list()
            
        elif order_option == '2':#allows a user to add a product to a list
            add_order()
            
        elif order_option == '3':#allows a user to select a product on the list and update it
            update_order()
            
        elif order_option == '4':#allows a user to select a product on the list and delete it
            remove_order()

        elif order_option == "0":
            main_menu()
            
        else:
            print("Invalid option, please select 0-4 from product options:")
            order_menu()

    except:
        print("Invalid option please select 0-4 from product options:")
        order_menu()
    order_menu()


#Takes user through the process of adding a new order record to the table
def add_order():
    query_new_customer()
    customer_list()
    customer = input("Please select the customer ID:\n")
    courier_list()
    courier = input("Please select courier ID:\n")
    status_list()
    status = input("Please select status ID:\n")
    add_order = """
                    INSERT INTO order(customer_id, courier_id, status)
                    VALUES(%s, %s, %s)
                    RETURNING order_id, customer_id, courier_id, status
                    """
    new_order_values = (customer, courier, status)
    cursor.execute(add_order, new_order_values)
    connection.commit()
    add_orderline()
    order_menu()

#Allows user to add each item from a customer order and matches it to the order ID from the parent order table
def add_orderline():
    while True:
        query_add_items = input("Would you like to add an item to the order (y/n):\n")
        if query_add_items == "y":
            order_list()
            query_order_id = input("Please select ID of order you would like to add to:\n")
            item = input("Please enter ID of product you would like to add to order:\n")
            add_orderline = """
                            INSERT INTO orderline(order_id, item)
                            VALUES(%s, %s)
                            RETURNING orderline_id, order_id, item
                            """
            new_orderline_values = (query_order_id, item)
            cursor.execute(add_orderline, new_orderline_values)
            connection.commit()
            continue
        elif query_add_items == "n":
            break
        else:
            print("Invalid option! Please select 'y' to add another item or 'n' to finish adding items:\n")
            continue

    order_menu()

#asks if the user would like to add an order to existing customer or create a new one
def query_new_customer():
    print("Here is the current customer list:\n")
    customer_list()
    while True:
        is_customer = input("Select 'e' to add order for an existing customer or 'n' to add a new customer:\n")
        if is_customer == "n":
            add_customer()
        elif is_customer == "e":
            break
        else:
            print("Invalid option! Please enter 'e' for an existing customer or 'n' to add a new customer:\n")
            continue

#Allows user to add a new customer to the customer table
def add_customer():
    customer_name = input("Please enter the customer name:\n")
    customer_address = input("Please enter customer address:\n")
    customer_phone = input("Please enter customer phone number:\n")

    add_customer = """
                    INSERT INTO customers(name, address, phone)
                    VALUES(%s, %s, %s)
                    RETURNING customer_id, name, address, phone
                    """
    new_customer_values = (customer_name, customer_address, customer_phone)
    cursor.execute(add_customer, new_customer_values)
    connection.commit()
    order_menu()



#Takes the user through the process of updating an existing order record
def update_order():
    order_list()
    query_order = input("Please select the order ID you would like to update:\n")
    get_order(query_order)
    while True:
        query_update_customer = input("Would you like to update the customer (y/n)?\n")
        if query_update_customer == "y":
            customer_list()
            customer = input("Please select the customer ID:\n")
            update_order_customer(customer, query_order)
            break
        elif query_update_customer == "n":
            break
        else:
            print("Invalid option! Please select 'y' to update the customer or 'n' to continue:\n")
            continue

    while True:
        query_update_courier = input("Would you like to update the courier (y/n)?\n")
        if query_update_courier == "y":
            courier_list()
            courier = input("Please select courier ID:\n")
            update_order_courier(courier, query_order)
            break
        elif query_update_courier == "n":
            break
        else:
            print("Invalid option! Please select 'y' to update the courier or 'n' to continue:\n")
            continue

    while True:
        query_update_status = input("Would you like to update the order status (y/n)? \n")
        if query_update_status == "y":
            status_list()
            status = input("Pleae select status ID:\n")
            update_order_status(status, query_order)
            break
        elif query_update_status == "n":
            break
        else:
            print("Invalid option! Please select 'y' to update status or 'n' to continue:\n")
            continue

    while True: 
        query_update_order = input("Would you like to update the order items (y/n)? \n")
        if query_update_order == "y":
            add_orderline()
            break
        elif query_update_order == "n":
            break
        else:
            print("Invalid option! Please select 'y' to add an order item or 'n' continue:\n")
            continue

#functions to update the parts of an existing order
def update_order_customer(customer_id, order_id):
    update_order_customer = """
                            UPDATE orders SET customer_id = %s
                            WHERE order_id = %s
                            """
    cursor.execute(update_order_customer, (customer_id, order_id, ))
    connection.commit()

def update_order_status(status_id, order_id):
    update_order_status = """
                            UPDATE orders SET status_id = %s
                            WHERE order_id = %s
                            """
    cursor.execute(update_order_status, (status_id, order_id, ))
    connection.commit()

def update_order_courier(courier_id, order_id):
    update_order_courier = """
                            UPDATE orders SET courier_id = %s
                            WHERE order_id = %s
                            """
    cursor.execute(update_order_courier, (courier_id, order_id, ))
    connection.commit()


#Executes functions to select and remove an order record based on user input
def remove_order():
    order_list()
    query_order = input("Please select the order you would like to remove:\n")
    get_order(query_order)
    delete_order_record(query_order)

#Removes an order record
def delete_order_record(order_id):
    remove_order = """
                            DELETE FROM orders
                            WHERE order_id = %s
                            """
    cursor.execute(remove_order, (order_id, ))
    connection.commit()
    print("Here is the updated orders list:\n")
    order_list()


#Gets the relevant order from the table, given the ID
def get_order(order_id):
    print_order_query = """
                            SELECT * FROM orders 
                            WHERE order_id = %s
                            """
    cursor.execute(print_order_query, (order_id, ))
    result = cursor.fetchall()
    for row in result:
        print(row)


#These functions print the lists of information from the relevant tables along with their IDs
def customer_list():
    customer = "SELECT * FROM customers"
    cursor.execute(customer)
    result = cursor.fetchall()
    for row in result:
        print(row)

def status_list():
    status = "SELECT * FROM status"
    cursor.execute(status)
    result = cursor.fetchall()
    for row in result:
        print(row)

def order_list():
    order = "SELECT * FROM orders"
    cursor.execute(order)
    result = cursor.fetchall()
    for row in result:
        print(row)

def orderline_list():
    orderline = "SELECT * FROM orderline"
    cursor.execute(orderline)
    result = cursor.fetchall()
    for row in result:
        print(row)