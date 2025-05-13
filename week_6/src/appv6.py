import psycopg2
import os
from dotenv import load_dotenv
from main_menu import *
from product_menu import *
from courier_menu import *
from order_menu import *

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


main_menu()

connection.commit()
cursor.close()
connection.close()