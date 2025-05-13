from main_menu_functions import *
from courier_menu_functions import *
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



def products_menu():
    print("-------------------------")
    print("PRODUCT MENU OPTIONS:")
    print("[1] - Print Products List")
    print("[2] - Add a Product")
    print("[3] - Update a Product")
    print("[4] - Remove a Product")
    print("[0] - Back to Main Menu")
    print("-------------------------")

#executes functions to allow user to edit data stored in products dictionary

    product_option = input("Please select an option:\n")
    try:
        if product_option == '1':#prints current product menu
            product_list()
            
        elif product_option == '2':#allows a user to add a product to a list
            add_product()
            
        elif product_option == '3':#allows a user to select a product on the list and update it
            update_product()
            
        elif product_option == '4':#allows a user to select a product on the list and delete it
            remove_product()

        elif product_option == "0":
            main_menu()
            
        else:
            print("Invalid option, please select 0-4 from product options:")
            products_menu()

    except:
        print("Invalid option please select 0-4 from product options:")
        products_menu()
    products_menu()


#allows user to add a new product to the product list
def add_product():
    product_name = input("Please enter new product name:")
    product_price = input("Please enter new product price:")
    add_product = """
                    INSERT INTO products(product_name, price)
                    VALUES(%s, %s)
                    RETURNING product_id, product_name, price
                    """
    new_product_values = (product_name, product_price)
    cursor.execute(add_product, new_product_values)
    connection.commit()
    print("Here is the updated product list:")
    product_list()
    products_menu()

#allows user to update the name and/or price of an existing product
def update_product():
    product_list()
    query_update_product = int(input("Please select the product ID you would like to update:\n"))
    get_product(query_update_product)
    while True: 
        yn_update_name = input("Would you like to update the product name (y/n)?\n")
        if yn_update_name == "y":
            new_product_name = input("Please enter new name for product:\n")
            update_name(new_product_name, query_update_product)
            break
        elif yn_update_name == "n":
            break
        else:
            print("Invalid input, please type y for yes or n for no.")
            continue
    while True:
        yn_update_price = input("Would you like to update product price (y/n)?\n")
        if yn_update_price == "y":
            new_product_price = float(input("Please enter new price for product:\n"))
            update_price(new_product_price, query_update_product)
            break
        elif yn_update_price == "n":
            break
        else: 
            print("Invalid input, please type y for yes or n for no.")
            continue
    connection.commit()
    print("Here is the updated product list:")
    product_list()
    products_menu()


#selects the specified product record from the table
def get_product(product_id):
    print_product_query = """
                            SELECT * FROM products 
                            WHERE product_id = %s
                            """
    cursor.execute(print_product_query, (product_id, ))
    result = cursor.fetchall()
    for row in result:
        print(row)
#updates the specified product name
def update_name(product_name, product_id):
    update_product_name = """
                            UPDATE products SET product_name = %s
                            WHERE product_id = %s
                            """
    cursor.execute(update_product_name, (product_name, product_id, ))
#updates the specified product price
def update_price(price, product_id):
    update_product_name = """
                            UPDATE products SET price = %s
                            WHERE product_id = %s
                            """
    cursor.execute(update_product_name, (price, product_id, ))


#allows user to delete the record of a product from the products table
def remove_product():
    product_list()
    query_remove_product = int(input("Please select the product ID you would like to remove:"))
    get_product(query_remove_product)
    delete_product_record(query_remove_product)
    connection.commit()
    print("Here is the updated product list:")
    product_list()
    products_menu()
#selects the specified product to be deleted and deletes it
def delete_product_record(product_id):
    remove_product = """
                        DELETE FROM products
                        WHERE product_id = %s
                        RETURNING product_id, product_name, price
                        """
    cursor.execute(remove_product, (product_id, ))
    connection.commit()


#prints the current records in products table
def product_list():
    products = "SELECT * FROM products"
    cursor.execute(products)
    result = cursor.fetchall()
    for row in result:
        print(row)

