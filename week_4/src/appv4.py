
#Import csv files containing products, couriers and orders and puts them into useable dictionaries

import csv
products = {}
with open("data\\products.csv", "r") as products_raw:
    reader=csv.DictReader(products_raw)
    products=list(reader)

couriers = {}
with open("data\\couriers.csv", "r") as couriers_raw:
    reader=csv.DictReader(couriers_raw)
    couriers=list(reader)

orders = {}
with open("data\\orders.csv", "r") as orders_raw:
    reader=csv.DictReader(orders_raw)
    orders=list(reader)

status = ["Pending", "Accepted", "Preparing", "Waiting for courier", "Out for delivery", "Delivered"]



#Functions that print the contents of products, couriers and orders

def product_list(): #Lists current products
    for num, item in enumerate(products):
        print('{}: {}'.format(num, item))

def courier_list(): #Lists current couriers
    for num, item in enumerate(couriers):
        print('{}: {}'.format(num, item))

def order_list(): #Lists current orders
    for num, item in enumerate(orders):
        print('{}: {}'.format(num, item))



#Prints main menu options and executes functions to guide user to other menus

def main_menu():
    print("-------------------------")
    print("MAIN MENU OPTIONS:")
    print("[1] - Products Menu")
    print("[2] - Orders Menu")
    print("[3] - Couriers Menu")
    print("[0] - Exit App")
    print("-------------------------")

    main_option = input("Please select and option from the menu:\n")
    try:
        if main_option.isdigit():
            main_option = int(main_option)
            if main_option == 1:
                products_menu()
            elif main_option == 2:
                orders_menu()
            elif main_option == 3:
                couriers_menu()
            elif main_option == 0:
                with open("data\\orders.csv", "w") as orders_raw:
                    writer=csv.DictWriter(orders_raw, fieldnames=["name", "address", "phone", "order", "status"])
                    writer.writeheader()
                    writer.writerows(couriers)
                
                exit()
            else:
                print("Invalid option!")
                main_menu()
        else:
            print("Invalid option!")
            main_menu()
    except Exception as ex:
        print("Invalid option!", ex)
        main_menu()


#FUNCTIONS FOR PRODUCTS MENU

#prints options for products menu
def products_menu():
    print("-------------------------")
    print("MAIN MENU OPTIONS:")
    print("[1] - Print Products List")
    print("[2] - Add a Product")
    print("[3] - Update a Product")
    print("[4] - Remove a Product")
    print("[0] - Back to Main Menu")
    print("-------------------------")

#executes functions to allow user to edit data stored in products dictionary

    product_option = input("Please select an option:\n")
    try:
        if product_option.isdigit():
            product_option = int(product_option)
            if product_option == 1:#prints current product menu
                product_list()
                
            elif product_option == 2:#allows a user to add a product to a list
                add_product()
                
            elif product_option == 3:#allows a user to select a product on the list and update it
                update_product()
                
            elif product_option == 4:#allows a user to select a product on the list and delete it
                remove_product()
                
            else:
                print("Invalid option!")
                products_menu()

    except:
        print("Invalid option!")
        products_menu()

#allows user to add a new product to the products list
def add_product():
    new_product_name = input("Please enter new product name:\n")
    new_product_price = input("Please enter new product price:\n")
    products.append({"name":new_product_name, "price": new_product_price})
    print("Here is the updated product list:\n")
    product_list()
    products_menu()

#allows user to select a product on the products list and updates it
def update_product():
    product_list()
    update_product_option = input("Which product would you like to update?:\n")
    try:
        if update_product_option.isdigit():
            update_product_option = int(update_product_option)
            if update_product_option in range(len(products)):
                update_product_name = input("Please enter new product name:\n")
                update_product_price = input("Please enter new product price:\n")
                updated_product = {"name":update_product_name, "price":update_product_price}
                products[update_product_option] = updated_product
                print("Here is the updated product list:\n")
                product_list()
            else:
                print("Invalid option!")
                update_product()
    except TypeError:
        print("Invalid option!")
        update_product()
    products_menu()

#allows user to select a product from the products list and remove it
def remove_product():
    product_list()
    remove_product_option = input("Which product would you like to remove?:\n")
    try:
        if remove_product_option.isdigit():
            remove_product_option = int(remove_product_option)
            if remove_product_option in range(len(products)):
                del products[remove_product_option]
                print("Here is the updated product list:\n")
                product_list()
            else:
                print("Invalid option!")
                remove_product()
    except:
        print("Invalid option!")
        remove_product()
    products_menu()


#FUNCTIONS FOR ORDERS MENU

#prints options for orders menu
def orders_menu():
    print("-------------------------")
    print("MAIN MENU OPTIONS:")
    print("[1] - Print Orders List")
    print("[2] - Add an order")
    print("[3] - Update an order")
    print("[4] - Remove an order")
    print("[0] - Back to Main Menu")
    print("-------------------------")

#executes functions to allow user to edit data stored in products dictionary
    order_option = input("Please select an option:\n")
    if order_option.isdigit():
        order_option = int(order_option)
        try:
            if order_option == 1:#prints current order list
                order_list()
            elif order_option == 2:#allows user to add a new order to the orders dicitonary
                add_order()
            elif order_option == 3:#allows user to select an order and update the details
                update_order()
            elif order_option == 4:#allows a user to select an order and delete it from the orders dictionary
                remove_order()
            elif order_option == 0:
                main_menu()
            else:
                print("Invalid option!")
            orders_menu()
        except:
            print("Invalid option!")
            orders_menu()

#allows user to add individual items to an order
def add_order_item():
    new_order = []
    product_list()
    order_item = input("Please select an item to add to order:\n")
    if order_item.isdigit():
        order_item = int(order_item)
        try:
            if order_item in range(len(products)):
                new_order.append(products[order_item])
                
            else:
                print("Invalid option!")
                add_order_item()
        except:
            print("Invalid option!")
    else:
        print("Invalid option!\n")
    try:
        more_items = input("Would you like to add more items? y/n\n")
        if (more_items == "y" or more_items =="Y"):
            add_order_item()
        elif (more_items == "n" or more_items == "N"):
            return new_order
            
        else:
            print("Invalid option!\n")
            add_order_item()
    except:
        print("Invalid option!")
        add_order_item()

#allows a user to add an order status
def add_order_status():
    new_status = []
    for num, item in enumerate(status):
        print('{}: {}'.format(num, item))
    try:
        new_status = input("Enter new order status:\n")
        if new_status.isdigit():
            new_status = int(new_status)
            if new_status in range(len(status)):
                return new_status
            else:
                print("Invalid option!")
                add_order_status()
        else:
            print("Invalid option!")
            add_order_status()
    except:
        print("Invalid option!")
        add_order_status()

#allows a user to add a courier 
def add_courier():
    new_courier = []
    courier_list()
    query_courier = input("Please select the courier to add to order:\n")
    if query_courier.isdigit():
        query_courier = int(query_courier)
        try:
            if query_courier in range(len(couriers)):
                new_courier.append(couriers[query_courier])
                return new_courier
            else:
                print("Invalid option!")
                add_courier()
        except Exception as ex:
            print("Invalid option!", ex)
            add_courier
    else:
        print("Invalid option!\n")
        add_courier()

#add an order to the orders dictionary
def add_order():
    #asks user for customer name
    name = input("Enter customer name:\n")

    #Function to add items to an order
    new_order = add_order_item()

    #adds order status to a new order
    new_status = add_order_status()

    #adds courier to a new order
    new_courier = add_courier()
    

    #adds user inputs to a new dictionary and then adds that to the orders list
    new_order_entry = {"name": name, "order": new_order, "status": new_status, "courier": new_courier}
    orders.append(new_order_entry)
    order_list()

#allows user to select an order to update
def update_order():

    #prints orders list
    order_list()

    #asks user to select order to update
    try:
        query_order = input("Please select order you would like to update:\n")
        if query_order.isdigit():
            query_order = int(query_order)
            if query_order in range(len(order_list)):
                new_status = query_order
            else:
                print("Invalid option!")
                update_order()
        else:
            print("Invalid option!")
            update_order()
    except:
        print("Invalid option!\n")
        update_order()
    
    #asks user for an updated customer name
    name = input("Please enter new customer name:\n")
    
    #asks user which items they want to add to the order
    new_order = add_order_item()
    
    #asks user to update the order status
    new_status = add_order_status()

    #asks user to update courier status
    new_courier = add_courier()

    #adds user data to a new variable and then replaces the chosen order with the new information
    new_order_entry = {"name": name, "order": new_order, "status": new_status, "courier": new_courier}
    orders[query_order].update(new_order_entry)

#allows user to remove an order
def remove_order():
     #prints orders list
    order_list()

    #asks user to select order to delete
    try:
        query_order = input("Please select order you would like to delete:\n")
        if query_order.isdigit():
            query_order = int(query_order)
            #removes the selected order from the orders list
            if query_order in range(len(order_list)):
               del orders[query_order] 
            else:
                print("Invalid option!")
                remove_order()
    except:
        print("Invalid option!\n")
        remove_order()


#FUNCTIONS FOR COURIERS MENU

def couriers_menu():

    print("-------------------------")
    print("MAIN MENU OPTIONS:")
    print("[1] - Print Couriers List")
    print("[2] - Add a Courier")
    print("[3] - Update a Courier")
    print("[4] - Remove a Courier")
    print("[0] - Back to Main Menu")
    print("-------------------------")

    option = input("Please select an option:\n")
    if option.isdigit():
        option = int(option)
        try:
            if option == 1:#prints current courier list
                courier_list()
            elif option == 2:#allows user to add a new order to the orders dicitonary
                add_new_courier()
            elif option == 3:#allows user to select an order and update the details
                update_courier()
            elif option == 4:#allows a user to select an order and delete it from the orders dictionary
                remove_courier()
            elif option == 0:
                main_menu()
            else:
                print("Invalid option!")
            orders_menu()
        except:
            print("Invalid option!")
            orders_menu()

#allows user to add a new courier to the couriers list
def add_new_courier():
    new_courier_company = input("Please enter new courier company:\n")
    new_courier_name = input("Please enter new courier name:\n")
    new_courier_phone = input("Please enter new courier contact number:\n")
    couriers.append({"company":new_courier_company, "name": new_courier_name, "phone": new_courier_phone})
    print("Here is the updated courier list:\n")
    courier_list()
    couriers_menu()

#allows user to update an existing courier with new information
def update_courier():
    courier_list()
    option = input("Which courier would you like to update?:\n")
    try:
        if option.isdigit():
            option = int(option)
            if option in range(len(couriers)):
                update_courier_company = input("Please enter new courier company:\n")
                update_courier_name = input("Please enter new courier name:\n")
                update_courier_phone = input("Please enter new courier contact number:\n")
                updated_courier = {"company": update_courier_company, "name": update_courier_name, "phone": update_courier_phone}
                couriers[option] = updated_courier
                print("Here is the updated couriers list:\n")
                courier_list()
            else:
                print("Invalid option!")
                update_courier()
    except TypeError:
        print("Invalid option!")
        update_courier()
    couriers_menu()

#allows user to select a courier to remove from couriers list
def remove_courier():
    courier_list()

    #asks user to select courier to delete
    try:
        query_order = input("Please select courier you would like to delete:\n")
        if query_order.isdigit():
            query_order = int(query_order)
            #removes the selected order from the orders list
            if query_order in range(len(courier_list)):
               del courier_list[query_order] 
            else:
                print("Invalid option!")
                remove_courier()
    except:
        print("Invalid option!\n")
        remove_courier()

main_menu()
