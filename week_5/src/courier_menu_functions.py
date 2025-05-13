from main_menu_functions import *
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

def courier_menu():
    print("-------------------------")
    print("COURIER MENU OPTIONS:")
    print("[1] - Print Couriers List")
    print("[2] - Add a Courier")
    print("[3] - Update a Courier")
    print("[4] - Remove a Courier")
    print("[0] - Back to Main Menu")
    print("-------------------------")

#executes functions to allow user to edit data stored in products dictionary

    product_option = input("Please select an option:\n")
    try:
        if product_option == '1':#prints current courier table
            courier_list()
            
        elif product_option == '2':#allows a user to add a courier to a list
            add_courier()
            
        elif product_option == '3':#allows a user to select a courier on the list and update it
            update_courier()
            
        elif product_option == '4':#allows a user to select a product on the list and delete it
            remove_courier()

        elif product_option == "0":
            main_menu()
            
        else:
            print("Invalid option, please select 0-4 from product options:")
            courier_menu()

    except:
        print("Invalid option please select 0-4 from product options:")
        courier_menu()
    courier_menu()

#adds a new courier record to the couriers table
def add_courier():
    courier_company = input("Please enter new courier company:\n")
    courier_name = input("Please enter new courier name:\n")
    courier_phone = input("Please enter a phoe number for the courier:\n")
    add_courier = """
                    INSERT INTO couriers(company, name, phone)
                    VALUES(%s, %s, %s)
                    RETURNING company, name, phone
                    """
    new_product_values = (courier_company, courier_name, courier_phone)
    cursor.execute(add_courier, new_product_values)
    connection.commit()
    print("Here is the updated couriers list:")
    courier_list()
    courier_menu()

#updates courier record details given user input
def update_courier():
    courier_list()
    query_update_courier = int(input("Please select the courier ID you would like to update:\n"))
    get_courier(query_update_courier)
    while True: 
        yn_update_company = input("Would you like to update the courier company (y/n)?\n")
        if yn_update_company == "y":
            new_courier_company = input("Please enter new company for courier:\n")
            update_company(new_courier_company, query_update_courier)
            break
        elif yn_update_company == "n":
            break
        else:
            print("Invalid input, please type y for yes or n for no.")
            continue
    while True:
        yn_update_name = input("Would you like to update courier name (y/n)?\n")
        if yn_update_name == "y":
            new_courier_name = input("Please enter new name for courier:\n")
            update_name(new_courier_name, query_update_courier)
            break
        elif yn_update_name == "n":
            break
        else: 
            print("Invalid input, please type y for yes or n for no.")
            continue
    while True:
        yn_update_phone = input("Would you like to update courier phone number (y/n)?\n")
        if yn_update_phone == "y":
            new_courier_phone = input("Please enter new number for courier:\n")
            update_phone(new_courier_phone, query_update_courier)
            break
        elif yn_update_phone == "n":
            break
        else: 
            print("Invalid input, please type y for yes or n for no.")
            continue
    connection.commit()
    print("Here is the updated product list:")
    courier_list()
    courier_menu()

#selects specified courier
def get_courier(courier_id):
    print_courier_query = """
                            SELECT * FROM couriers
                            WHERE courier_id = %s
                            """
    cursor.execute(print_courier_query, (courier_id, ))
    result = cursor.fetchall()
    for row in result:
        print(row)

#updates company for specified courier
def update_company(company, courier_id):
    update_courier_company = """
                            UPDATE couriers SET company = %s
                            WHERE courier_id = %s
                            """
    cursor.execute(update_courier_company, (company, courier_id, ))

#updates name for specified courier
def update_name(name, courier_id):
    update_courier_name = """
                            UPDATE couriers SET name = %s
                            WHERE courier_id = %s
                            """
    cursor.execute(update_courier_name, (name, courier_id, ))

#updates phone number for specified courier
def update_phone(phone, courier_id):
    update_courier_phone = """
                            UPDATE couriers SET phone = %s
                            WHERE courier_id = %s
                            """
    cursor.execute(update_courier_phone, (phone, courier_id, ))

#asks user to specify courier to remove and then deletes it from the couriers table
def remove_courier():
    courier_list()
    query_remove_courier = int(input("Please select the courier ID you would like to remove:"))
    get_courier(query_remove_courier)
    delete_courier_record(query_remove_courier)
    connection.commit()
    print("Here is the updated product list:")
    courier_list()
    courier_menu()

#deletes specified courier record
def delete_courier_record(courier_id):
    remove_courier = """
                        DELETE FROM couriers
                        WHERE courier_id = %s
                        RETURNING courier_id, company, name, phone
                        """
    cursor.execute(remove_courier, (courier_id, ))
    connection.commit()

#prints a list of current courier records
def courier_list():
    couriers = "SELECT * FROM couriers"
    cursor.execute(couriers)
    result = cursor.fetchall()
    for row in result:
        print(row)