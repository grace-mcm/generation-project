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

def add_new_customer(name, address, phone):
    add_customer = """
                    INSERT INTO customers(name, address, phone)
                    VALUES(%s, %s, %s)
                    RETURNING customer_id, name, address, phone
                    """
    new_customer_values = (name, address, phone)
    cursor.execute(add_customer, new_customer_values)
    connection.commit()

def add_new_order(customer, courier, status):
    add_order = """
                    INSERT INTO order(customer_id, courier_id, status)
                    VALUES(%s, %s, %s)
                    RETURNING order_id, customer_id, courier_id, status
                    """
    new_order_values = (customer, courier, status)
    try:
        cursor.execute(add_order, new_order_values)
        connection.commit()
    except:
        print("Error adding order!")

def add_new_orderline(order_id, item):
    add_orderline = """
                            INSERT INTO orderline(order_id, item)
                            VALUES(%s, %s)
                            RETURNING orderline_id, order_id, item
                            """
    new_orderline_values = (order_id, item)
    cursor.execute(add_orderline, new_orderline_values)
    connection.commit()

def view_orderline():
    if input("Would you like to see the details of an order? (y/n)").lower() == "y":
        orderline_query = int(input("Please select the ID of the order you would like to view:\n"))
        get_orderline(orderline_query)
        
def get_orderline(order_id):
    print_orderline = """
                        SELECT * FROM orderline
                        WHERE order_id = %s"""  
    cursor.execute(print_orderline, (order_id))
    result = cursor.fetchall()
    for row in result:
        print(row)

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

#Allows user to update the customer for an order record
def update_order_customer(customer_id, order_id):
    update_order_customer = """
                            UPDATE orders SET customer_id = %s
                            WHERE order_id = %s
                            """
    cursor.execute(update_order_customer, (customer_id, order_id, ))
    connection.commit()

#Allows user to update the status of an order record
def update_order_status(status_id, order_id):
    update_order_status = """
                            UPDATE orders SET status_id = %s
                            WHERE order_id = %s
                            """
    cursor.execute(update_order_status, (status_id, order_id, ))
    connection.commit()

#Allows user to update courier for an order record
def update_order_courier(courier_id, order_id):
    update_order_courier = """
                            UPDATE orders SET courier_id = %s
                            WHERE order_id = %s
                            """
    cursor.execute(update_order_courier, (courier_id, order_id, ))
    connection.commit()

#Prints current list of order records
def order_list():
    order = "SELECT * FROM orders"
    cursor.execute(order)
    result = cursor.fetchall()
    for row in result:
        print(row)

#Prints current list of customer records
def customer_list():
    customer = "SELECT * FROM customers"
    cursor.execute(customer)
    result = cursor.fetchall()
    for row in result:
        print(row)

#Prints status options
def status_list():
    status = "SELECT * FROM status"
    cursor.execute(status)
    result = cursor.fetchall()
    for row in result:
        print(row)

#Prints current list of order records
def orderline_list():
    orderline = "SELECT * FROM orderline"
    cursor.execute(orderline)
    result = cursor.fetchall()
    for row in result:
        print(row)