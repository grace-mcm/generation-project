from courier_db_utils import (get_courier, update_company, update_name, update_phone, delete_courier_record, courier_list, add_new_courier)
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
    while True:
        print("-------------------------")
        print("COURIER MENU OPTIONS:")
        print("[1] - Print Couriers List")
        print("[2] - Add a Courier")
        print("[3] - Update a Courier")
        print("[4] - Remove a Courier")
        print("[0] - Back to Main Menu")
        print("-------------------------")

#executes functions to allow user to edit data stored in products dictionary

        courier_option = input("Please select an option:\n")
        if courier_option == '1':#prints current courier table
            courier_list() 
        elif courier_option == '2':#allows a user to add a courier to a list
            add_courier()
        elif courier_option == '3':#allows a user to select a courier on the list and update it
            update_courier()
        elif courier_option == '4':#allows a user to select a product on the list and delete it
            remove_courier()
        elif courier_option == "0":
            from main_menu import main_menu
            main_menu()
            break
        else:
            print("Invalid option, please select 0-4 from product options:")


#adds a new courier record to the couriers table
def add_courier():
    courier_company = input("Please enter new courier company:\n")
    courier_name = input("Please enter new courier name:\n")
    courier_phone = input("Please enter a phoe number for the courier:\n")
    add_new_courier(courier_company, courier_name, courier_phone)
    print("Here is the updated couriers list:")
    courier_list()
    
#updates courier record details given user input
def update_courier():
    courier_list()
    try: 
        query_update_courier = int(input("Please select the courier ID you would like to update:\n"))
        get_courier(query_update_courier)

        if input("Would you like to update the courier company (y/n)?\n").lower() == "y":
            new_courier_company = input("Please enter new company for courier:\n")
            update_company(new_courier_company, query_update_courier)

        if input("Would you like to update courier name (y/n)?\n").lower() == "y":
            new_courier_name = input("Please enter new name for courier:\n")
            update_name(new_courier_name, query_update_courier)
        
        if input("Would you like to update courier phone number (y/n)?\n").lower() == "y":
            new_courier_phone = input("Please enter new number for courier:\n")
            update_phone(new_courier_phone, query_update_courier)

        connection.commit()
        print("Here is the updated product list:")
        courier_list()
    except:
        print("Invalid option!")


#asks user to specify courier to remove and then deletes it from the couriers table
def remove_courier():
    courier_list()
    try:
        query_remove_courier = int(input("Please select the courier ID you would like to remove:"))
        get_courier(query_remove_courier)
        delete_courier_record(query_remove_courier)
        connection.commit()
        print("Here is the updated product list:")
        courier_list()
    except:
        print("Invalid option!")