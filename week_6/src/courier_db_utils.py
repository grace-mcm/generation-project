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

def add_new_courier(courier_company, courier_name, courier_phone):
    add_courier = """
                    INSERT INTO couriers(company, name, phone)
                    VALUES(%s, %s, %s)
                    RETURNING company, name, phone
                    """
    new_product_values = (courier_company, courier_name, courier_phone)
    try:
        cursor.execute(add_courier, new_product_values)
        connection.commit()
    except: 
        print("Error adding courier!")

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
