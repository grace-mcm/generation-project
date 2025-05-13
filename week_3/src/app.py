
products = []
with open("data\\products.txt", "r") as products_raw:
    for product in products_raw:
        product = product.rstrip()
        products.append(product)

couriers = []
with open("data\\couriers.txt", "r") as couriers_raw:
    for courier in couriers_raw:
        courier = courier.rstrip()
        couriers.append(courier)

orders_list = [{"name":"Grace", "order":["chicken", "veggie"], "status":"Accepted"}, {"name":"Brian", "order":["veggie"], "status":"Preparing"}, {"name":"Poppy", "order":["veggie"], "status":"Preparing"}]

order_status = ["Pending", "Accepted", "Preparing", "Waiting for courier", "Out for delivery", "Delivered"]
    
def main_menu():#MAIN MENU OPTIONS
    print("--------------------------\nMAIN MENU OPTIONS:\n0 - Exit App\n1 - Products Menu\n2 - Orders Menu\n3 - Couriers Menu\n--------------------------")

def order_menu():#ORDER MENU OPTIONS
    print("--------------------------\nORDER MENU OPTIONS:\n0 - Return to Main Menu\n1 - Print Orders Dictionary\n2 - Create New Order\n3 - Update Existing Order Status\n4 - Update Existing Order\n5 - Delete Order\n--------------------------")

def product_menu(): #PRODUCT MENU OPTIONS
    print("--------------------------\nPRODUCT MENU OPTIONS:\n0 - Return to Main Menu\n1 - Current product list\n2 - Add a product\n3 - Update a product\n4 - Remove a product\n--------------------------")

def courier_menu():#COURIER MENU OPTIONS
    print("--------------------------\nCOURIER MENU OPTIONS:\n0 - Return to Main Menu\n1 - Print Courier List\n2 - Add a Courier\n3 - Update a Courier\n4 - Remove a Courier\n--------------------------")

def product_list(): #Lists current products
    print("\n".join(products))

def courier_list():
    print("\n".join(couriers))

def print_order_list():
    for orders in orders_list:
        print(f"{orders}\n")

def main_menu_sel():#MAIN MENU SELECTION
    while True:
        main_menu()
        user_input = (input("Please select an option:\n"))
        if user_input == "0":#EXIT APP
            with open("data\\products.txt", "w") as products_raw:
                for product in products:
                    products_raw.write(product+"\n")
            with open("data\\couriers.txt", "w") as couriers_raw:
                for courier in couriers:
                    couriers_raw.write(courier+"\n")
            exit()
            break
        elif user_input == "1":#PRINT PRODUCT MENU
            prod_menu_sel()
            continue
        elif user_input == "2":#PRINT ORDER MENU
            order_menu_sel()
            continue
        elif user_input == "3":#PRINT COURIER MENU
            courier_menu_sel()
            break
        else:
            print("Invalid selection, please select from list (0, 1, etc).")
            continue


def prod_menu_sel(): #PRODUCTS MENU SELECTION
    while True:
        product_menu()
        user_input = (input("Please select an option:\n"))
        if user_input == "0":#EXIT TO MAIN MENU
            main_menu_sel()
            break

        elif user_input == "1": #LIST CURRENT PRODUCTS
            print("Here is a list of products currently available:")
            product_list()
            continue

        elif user_input == "2": #ADD A PRODUCT
            newproduct = input("What product would you like to add?\n")
            products.append(newproduct)
            with open("data\\products.txt", "w") as products_raw:
                for product in products:
                    products_raw.write(product+"\n")
            print("Here is the updated product list:")
            product_list()
            continue

        elif user_input == "3": #UPDATE A PRODUCT
            for num, item in enumerate(products):
                print('{}: {}'.format(num, item))
            while True:
                try:
                    user_input = int(input("What product would you like to update?\n"))
                    if user_input in range(len(products)):
                        break
                    else:
                      print("Invalid option, please select from the list (e.g. 0, 1, etc)")  
                except:
                    print("Invalid option, please select from the list (e.g. 0, 1, etc)")
                    continue
            new_item = input("What would you like to replace this product with?\n")
            products[user_input] = new_item
            with open("data\\products.txt", "w") as products_raw:
                for product in products:
                    products_raw.write(product+"\n")
            print("Here is the updated product list:")
            product_list()
            continue

        elif user_input == "4": #REMOVE A PRODUCT
            for num, item in enumerate(products):
                print('{}: {}'.format(num, item))
            while True:
                try:
                    remove_item = int(input("What product would you like to remove?\n"))
                    if remove_item in range(len(products)):
                        break
                    else:
                      print("Invalid option, please select from the list (e.g. 1, 2, etc)")  
                except:
                    print("Invalid option, please select from the list (e.g. 1, 2, etc)")
                    continue
            del products[remove_item]
            with open("data\\products.txt", "w") as products_raw:
                for product in products:
                    products_raw.write(product+"\n")
            print("Here is the updated product list:")
            product_list()
            continue

        else:#PRINT INVALID OPTION, LOOP TO PRINT PRODUCT MENU
            print("Invalid selection, please select from list (0, 1, etc).")
            continue

def order_menu_sel():#ORDER MENU SELECTION
    while True:
        order_menu()
        order_input = (input("Please select an option from the menu:\n"))

        if order_input == "0":
            main_menu_sel()
            break

        elif order_input == "1":#PRINT CURRENT ORDERS
            print_order_list()
            continue

        elif order_input == "2":#ADD A NEW ORDER
            name = input("Please enter name of customer:\n")#ADDS CUSTOMER NAME
            for num, item in enumerate(products):
                print('{}: {}'.format(num, item))
            order_details = []

            while True:
                while True:
                    try:
                        order_details_select = int(input("Please select menu item to add to order:\n"))#ADDS ITEMS TO AN ORDER
                        if order_details_select in range(len(products)):
                            order_details.append(products[order_details_select])
                            
                        else:
                            print("Invalid option, please select from the list (e.g. 1, 2, etc)")
                            continue
                    except:
                        print("Invalid option, please select from the list (e.g. 1, 2, etc)")
                        continue
                    try:
                        add_more_order_details = input("Would you like to add more items to to the order? (y/n):\n")
                        if add_more_order_details == "y":#CONTINUE CODE TO ADD MORE ITEMS TO THE ORDER
                            continue
                        elif add_more_order_details == "n":#CONTINUES TO UPDATE STATUS
                            break
                        else:
                            print("Invalid option, please enter 'y' for yes or 'n' for no:\n")
                            continue
                    except:
                        print("Invalid option, please enter 'y' for yes or 'n' for no:\n")
                        continue
                break

            for num, item in enumerate(order_status):
                print('{}: {}'.format(num, item))
            status = " "
            while True:
                try:
                    new_status = int(input("Please enter order status:\n"))#ADDS STATUS TO NEW ORDER
                    if new_status in range(len(order_status)):
                        status = f"{(order_status[new_status])}"
                        break
                    else:
                        print("Invalid option, please select from the list (e.g. 1, 2, etc)")
                        continue
                except:
                    print("Invalid option, please select from the list (e.g. 1, 2, etc)")

            new_order = {"name":name, "order":order_details, "status":status}
            orders_list.append(new_order)
            print_order_list()
            break

        elif order_input == "3":#UPDATE ORDER STATUS
            while True:
                try:
                    continue_update_status = input("Would you like to update an order status (y/n)?:\n")#CONFIRM IF USER WANTS TO UPDATE AN ORDER
                    if continue_update_status == "y":
                        for num, item in enumerate(orders_list):
                            print('{}: {}'.format(num, item))
                        while True:
                            try:
                                status_input = int(input("Which order would you like to update the status of?\n"))#ASKS WHICH ORDER USER WANTS TO UPDATE BY INDEX
                                if status_input in range(len(orders_list)):
                                    break
                                else:
                                    print("That is not a valid option, please select option from list (eg 0, 1, etc)\n")
                                    continue
                            except:
                                print("That is not a valid option, please select option from list (eg 0, 1, etc)\n")
                                continue
                        for num, item in enumerate(order_status):
                            print('{}: {}'.format(num, item))
                        while True:
                            try:
                                status_select = input("Please select new order status:\n")#ASKS USER WHICH STATUS THEY WOULD LIKE TO ADD
                                for orders_list[status_input] in orders_list:
                                    if status_select == "0":#UPDATES TO PENDING
                                        updated_order_status = {"status" : order_status[0]}
                                        orders_list[status_input].update(updated_order_status)
                                        print_order_list()
                                        break
                                    
                                    elif status_select == "1":#UPDATES TO ACCEPTED
                                        updated_order_status = {"status" : order_status[1]}
                                        orders_list[status_input].update(updated_order_status)
                                        print_order_list()
                                        break
                                    
                                    elif status_select == "2":#UPDATES TO PREPARING
                                        updated_order_status = {"status" : order_status[2]}
                                        orders_list[status_input].update(updated_order_status)
                                        print_order_list()
                                        break
                                    
                                    elif status_select == "3":#UPDATES TO WAITING FOR COURIER
                                        updated_order_status = {"status" : order_status[3]}
                                        orders_list[status_input].update(updated_order_status)
                                        print_order_list()
                                        break
                                    
                                    elif status_select == "4":#UPDATES TO OUT FOR DELIVERY
                                        updated_order_status = {"status" : order_status[4]}
                                        orders_list[status_input].update(updated_order_status)
                                        print_order_list()
                                        break
                                    
                                    elif status_select == "5":#UPDATES TO DELIVERED
                                        updated_order_status = {"status" : order_status[5]}
                                        orders_list[status_input].update(updated_order_status)
                                        print_order_list()
                                        break
                                    
                                    else:
                                        print("That is not a valid option, please select option from list (eg 0, 1, etc)\n")
                                        continue
                                else:
                                    print("That is not a valid option, please select option from list (eg 0, 1, etc)\n")
                                    continue
                            except:
                                print("That is not a valid option, please select option from list (eg 0, 1, etc)\n")
                                continue
                            break
                    elif continue_update_status == "n":#LOOPS TO PRINT ORDER MENU
                        order_menu_sel()
                        break
                    else:
                        print("That is not a valid option, please select option from list (eg 0, 1, etc)\n")
                        continue
                except:
                    print("That is not a valid option, please select option from list (eg 0, 1, etc)\n")
                    continue     

        elif order_input == "4":#UPDATE AN ORDER
            for num, item in enumerate(orders_list):
                print('{}: {}'.format(num, item))
            query_updated_order = int(input("Which order would you like to update?\n"))#ASKS USER TO SELECT ORDER BY INDEX
            if query_updated_order in range(len(orders_list)):
                while True:

                    try:#ASKS IF THE USER WANTS TO CHANGE THE CUSTOMER NAME
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

                    try:#ASKS IF THE USER WANTS TO UPDATE THE ORDER ITEMS
                        query_order_update = input("Would you like to update the customer order?\n")#CONFIRMS USER WANTS TO UPDATE ORDER
                        if query_order_update == "y":
                            for num, item in enumerate(products):
                                print('{}: {}'.format(num, item))
                            order_details = []

                            while True:#LOOPS THROUGH ADDING MORE ITEMS TO THE ORDER 
                                order_details_select = int(input("Please select menu item to add to order:\n"))
                                order_details.append(products[order_details_select])
                                add_more_order_details = input("Would you like to add more items to to the order? (y/n):\n")
                                if add_more_order_details == "y":
                                    continue
                                elif add_more_order_details == "n":
                                    break

                        elif query_order_update == "n":#UPDATES ORDER AND GOES BACK TO ORDER MENU
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
            break

        elif order_input == "5":#DELETE AN ORDER
            for num, item in enumerate(orders_list):
                print('{}: {}'.format(num, item))
            query_delete_order = int(input("Which order would you like to delete?\n"))
            if query_delete_order in range(len(orders_list)):
                del orders_list[query_delete_order]
                print("Here is the updated order list:")
                print(orders_list)
                break
            else:
                print("Invalid selection, please select from list (0, 1, etc).")
                continue

        else:
            print("Invalid selection, please select from list (0, 1, etc).")
            continue

def courier_menu_sel():#COURIER MENU SELECTION
    while True:
        courier_menu()
        courier_input = input("Please select an option from the menu:\n")

        if courier_input == "0":#Back to main menu
            main_menu_sel()
            break

        elif courier_input == "1":#Print courier list
            courier_list()
            continue

        elif courier_input == "2":#Add a courier
            new_courier = input("Please input the name of the new courier:\n")
            couriers.append(new_courier)
            with open("data\\couriers.txt", "w") as couriers_raw:
                for courier in couriers:
                    couriers_raw.write(courier+"\n")
            print("Here is the updated courier list:")
            courier_list()
            continue

        elif courier_input == "3":#Update a courier
            for num, item in enumerate(couriers):
                print('{}: {}'.format(num, item))
            new_courier_query = int(input("Please select which courier you would like to update:\n"))
            new_courier = input("Please enter the updated courier:\n")
            couriers[new_courier_query] = new_courier
            with open("data\\couriers.txt", "w") as couriers_raw:
                for courier in couriers:
                    couriers_raw.write(courier+"\n")
            print("Here is the updated courier list:")
            courier_list()
            continue

        elif courier_input == "4":#Delete a courier
            for num, item in enumerate(couriers):
                print('{}: {}'.format(num, item))
            delete_courier_query = int(input("Please select which courier you would like to delete:\n"))
            del couriers[delete_courier_query]
            with open("data\\couriers.txt", "w") as couriers_raw:
                for courier in couriers:
                    couriers_raw.write(courier+"\n")
            print("Here is the updated courier list:\n")
            courier_list()
            continue

        else:
            print("Invalid selection, please select from list (0, 1, etc).")
            continue

main_menu_sel()
    
    
    
