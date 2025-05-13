import psycopg2
import os
from dotenv import load_dotenv
import csv
from main_menu_functions import *
from product_menu_functions import *
from courier_menu_functions import *


status = ["Pending", "Accepted", "Preparing", "Waiting for courier", "Out for delivery", "Delivered"]

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



connection.commit()
cursor.close()
connection.close()