products = ["chicken", "fish", "veggie", "vegan", "dietary"]

orders_list = [{"name":"Grace", "order":["chicken", "veggie"], "status":"Accepted"}, {"name":"Brian", "order":["veggie"], "status":"Preparing"}, {"name":"Poppy", "order":["veggie"], "status":"Preparing"}]

order_status = ["Pending", "Accepted", "Preparing", "Waiting for courier", "Out for delivery", "Delivered"]

def main_menu():#Shows options in main menu
    print("0 - Exit App\n1 - Products Menu\n2 - Orders Menu")

def order_menu():#Shows options in order menu
    print("0 - Return to Main Menu\n1 - Print Orders Dictionary\n2 - Create New Order\n3 - Update Existing Order Status\n4 - Update Existing Order\n5 - Delete Order")

def product_menu(): #Shows the options in the product menu
    print("0 - Return to Main Menu\n1 - Current product list\n2 - Add a product\n3 - Update a product\n4 - Remove a product")

def main_menu_sel():#Accepts user input and executes defined functions based on main menu selection
    while True:
        main_menu()
        user_input = (input("Please select an option:\n"))
        if user_input == "0":
            exit()
            break
        elif user_input == "1":
            prod_menu_sel()
            continue
        elif user_input == "2":
            order_menu_sel()
            break
        else:
            print("Invalid selection, please select from list (0, 1, etc).")
            continue


def product_list(): #Lists current products
    print("\n".join(products))
          

def prod_menu_sel(): #Accepts user input and executes defined functions based on product menu selection
    while True:
        product_menu()
        user_input = (input("Please select an option:\n"))
        if user_input == "0":
            main_menu_sel()
            break

        elif user_input == "1": #Lists current products list
            print("Here is a list of products currently available:")
            newproduct = input("What product would you like to add?\n")
            products.append(newproduct)
            print("Here is the updated product list:")
            product_list()
            continue

        elif user_input == "2": #Allows user to add a product to product list
            newproduct = input("What product would you like to add?\n")
            products.append(newproduct)
            print("Here is the updated product list:")
            product_list()
            continue

        elif user_input == "3": #Allows user to update a product from the product list
            for num, item in enumerate(products):
                print('{}: {}'.format(num, item))
            user_input = int(input("What product would you like to update?\n"))
            new_item = input("What would you like to replace this product with?\n")
            products[user_input] = new_item
            print("Here is the updated product list:")
            product_list()
            continue

        elif user_input == "4": #Allows user to remove a product from the product list
            for num, item in enumerate(products):
                print('{}: {}'.format(num, item))
            remove_item = int(input("What product would you like to remove?\n"))
            del products[remove_item]
            print("Here is the updated product list:")
            product_list()
            continue

        else:
            print("Invalid selection, please select from list (0, 1, etc).")
            continue



def order_dict():
    print(f"{orders_list}")

def new_order():#Allows user to create a new order and add it to the orders list
    name = input("Please enter name of customer:\n")
    for num, item in enumerate(products):
        print('{}: {}'.format(num, item))
    order_details = []
    while True:
        order_details_select = int(input("Please select menu item to add to order:\n"))
        order_details.append(products[order_details_select])
        add_more_order_details = input("Would you like to add more items to to the order? (y/n):\n")
        if add_more_order_details == "y":
            continue
        elif add_more_order_details == "n":
            break
    for num, item in enumerate(order_status):
        print('{}: {}'.format(num, item))
    status = " "
    new_status = int(input("Please enter order status:\n"))
    status = f"{(order_status[new_status])}"
    new_order = {"name":name, "order":order_details, "status":status}
    orders_list.append(new_order)
    print(orders_list)

def update_order_status():#Allows user to select an order and update the delivery status
    while True:
        continue_update_status = input("Would you like to update an order status (y/n)?:\n")
        if continue_update_status == "y":
            for num, item in enumerate(orders_list):
                print('{}: {}'.format(num, item))
            status_input = int(input("Which order would you like to update the status of?\n"))
            for num, item in enumerate(order_status):
                print('{}: {}'.format(num, item))
            status_select = input("Please select new order status:\n")
            for orders_list[status_input] in orders_list:
                if status_select == "0":
                    updated_order_status = {"status" : order_status[0]}
                    orders_list[status_input].update(updated_order_status)
                    print(orders_list)
                    continue

                elif status_select == "1":
                    updated_order_status = {"status" : order_status[1]}
                    orders_list[status_input].update(updated_order_status)
                    print(orders_list)
                    continue

                elif status_select == "2":
                    updated_order_status = {"status" : order_status[2]}
                    orders_list[status_input].update(updated_order_status)
                    print(orders_list)
                    continue

                elif status_select == "3":
                    updated_order_status = {"status" : order_status[3]}
                    orders_list[status_input].update(updated_order_status)
                    print(orders_list)
                    continue

                elif status_select == "4":
                    updated_order_status = {"status" : order_status[4]}
                    orders_list[status_input].update(updated_order_status)
                    print(orders_list)
                    continue

                elif status_select == "5":
                    updated_order_status = {"status" : order_status[5]}
                    orders_list[status_input].update(updated_order_status)
                    print(orders_list)
                    continue

                else:
                    print("That is not a valid option, please select option from list (eg 0, 1, etc)\n")
                    continue
        elif continue_update_status == "n":
            order_menu_sel()

def update_order():#Allows user to select an order and update the name and order details
    for num, item in enumerate(orders_list):
        print('{}: {}'.format(num, item))
    query_updated_order = int(input("Which order would you like to update?\n"))
    while True:
        try:
            query_name_update = input("Would you like to update the name of the customer?:\n")
            if query_name_update == "y":
                name_update = input("Please enter new customer name:\n")
                break
            elif query_name_update == "n":
                name_update = orders_list[query_updated_order]["name"]
                break
            else:
               print("Invalid selection, please enter 'y' or 'n':\n")
               continue
        except:
            print("Invalid selection, please enter 'y' or 'n':\n")
            continue
    while True:
        try:
            query_order_update = input("Would you like to update the customer order?\n")
            if query_order_update == "y":
                for num, item in enumerate(products):
                    print('{}: {}'.format(num, item))
                order_details = []
                while True:
                    order_details_select = int(input("Please select menu item to add to order:\n"))
                    order_details.append(products[order_details_select])
                    add_more_order_details = input("Would you like to add more items to to the order? (y/n):\n")
                    if add_more_order_details == "y":
                        continue
                    elif add_more_order_details == "n":
                        break
            elif query_order_update == "n":
                order_details = orders_list[query_updated_order]["order"]
                break
            else:
               print("Invalid option, please enter 'y' or 'n':\n")
               continue
        except:
            print("Invalid option, please enter 'y' or 'n':\n")
            continue
        break
    updated_order = {"name":name_update, "order":order_details}
    orders_list[query_updated_order].update(updated_order)
    print(orders_list)

def order_menu_sel():#Accepts user input and executes defined functions based on order menu selection
    while True:
        order_menu()
        order_input = (input("Please select an option from the menu:\n"))
        if order_input == "0":
            main_menu_sel()
            break
        elif order_input == "1":
            order_dict()
            continue
        elif order_input == "2":
            new_order()
            continue
        elif order_input == "3":
            update_order_status()
        elif order_input == "4":
            update_order()
            continue
        elif order_input == "5":
            delete_order()
            continue
        else:
            print("Invalid selection, please select from list (0, 1, etc).")
            continue

main_menu_sel()