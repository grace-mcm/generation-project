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


#selects the specified product record from the table
def get_product(product_id):
    print_product_query = """
                            SELECT * FROM products 
                            WHERE product_id = %s
                            """
    cursor.execute(print_product_query, (product_id, ))
    result = cursor.fetchall()
    if result:
        print(result)
    else:
        print("Product not found.")

def add_new_product(product_name, product_price):
    add_product_db = """INSERT INTO products(product_name, price) VALUES(%s, %s) RETURNING product_id, product_name, price"""
    new_product_values = (product_name, product_price)
    try: 
        cursor.execute(add_product_db, new_product_values)
        print("Execute was successul")
        connection.commit()
        print("commit was successful")
    except Exception as e:
        print("Unable to add product!")
        print(f"Error: {e}")

#updates the specified product name
def update_product_name(product_name, product_id):
    update_product_name = """
                            UPDATE products SET product_name = %s
                            WHERE product_id = %s
                            """
    cursor.execute(update_product_name, (product_name, product_id, ))
    connection.commit()

#updates the specified product price
def update_product_price(price, product_id):
    update_product_name = """
                            UPDATE products SET price = %s
                            WHERE product_id = %s
                            """
    cursor.execute(update_product_name, (price, product_id, ))
    connection.commit()

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