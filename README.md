# Grace's Mini Project

## WHAT IS THE PROJECT FOR?

This project was set up to meet the needs of a cafe that wanted to fulfil lunch orders for the surrounding offices.

The cafe wanted a back end app to:
* Create and manage a products list
* Create and manage a couriers list
* Create and manage customer orders

For each of these features, they wanted to be able to:
* View the current entries in each section
* Add a new entry
* Update an existing entry
* Delete an existing entry

They also wanted the products, orders and couriers they entered to persist once the app was closed

## FILE STRUCTURE

![alt text](<menu structure.png>)

My app is split into several menus to make it easier to navigate. Each menu has been broken out into separate modules containing their specific functions, and each menu has a corresponding database utilities folder which handles the database queries. I did this to make my code modular, simpler to navigate and easier to test.  

### appv6.py
This is my main executable file that will run the rest of my code

### Menu Functions Files
I have separated my menus into courier_menu, main_menu, order_menu and product_menu. These files contain the code to make these menus work and I have imported them as modules into the main app file. 

### db_utils.py
These files contain the functions for each menu that access the database I have created. I separated them to streamline my code and keep it modular and because my code was getting very long. 

### Test
This folder contains all the tests I have written to make sure that my code is working in the way it was intended. 

## HOW DOES IT WORK?

### Database access and imported modules

![alt text](<database access.png>)

At the beginning of my appv6.py file, I have created a connection to my database and have imported the necessary libraries to make it work. As I have stored my menu functions in separate files, I also needed to import them into the main app so that the menus work. 

### Main Menu

![alt text](<main menu functions.png>)

My menu structures all follow the same basic structure: they print the main menu options and are asked to input which numbered option they would like. The function then takes this input and runs it through an if statement to execute the relevant menu function. If the user inputs something that is not one of the menu options, it will throw back an error message and loop the user back to the beginning.

I have encased the if statement into a while loop so that the menu will continue to run until the user exits the application. As I am interacting with a database, I have included two statements to commit any changes made to the database and close the connection and the cursor so that the database doesn't stay connected in the background. 

### Products Menu

![alt text](<products menu.png>)

My products menu is similar to my main menu in structure and works in much the same way, except that the exit option loops the user back to the main menu instead of exiting the entire application. I have included the main features that were required for the project: list, add, update and delete.

### Adding functions

![alt text](<add product.png>)

All of my menu functions for adding something to the database follow the same structure. They:

1. Create variables with the assigned value of user input, specifying details of the new object. e.g. to add a new product, the function asks the user for a product name and price as these are the fields specfified in the product table for a new object.
2. Runs the variable "add_<"object">()" which accesses the database, calls the specific table with INSERT INTO and specifies which value fields it requires. The VALUES parameters are left empty so that they can be filled with the user input recorded above. It then returns the new record values. 
3. A new variable is created to contain the user input values so that they can be called together later in the function. This is because cursor.execute() only allows two arguments - the action ("add_<"object">()") and the values (variables containing user input for the new object).
4. cursor.execute() interacts with the database to complete the action that has been given as an argument. It takes the second argument as values and applies it to the first if there are blank parameters. 
5. connection.commit() saves the changes made to the database immediately so that if the system crashes or there is an unexpected error the data is safe. 
6. Finally, it prints the update list with the new record included. 

The cursor and connection steps are encased in try except so that if there is an error with adding the data to the table, it will inform the user that there was a mistake. 

### Updating Functions

![alt text](<update courier function.png>)

As with most of my code, the update functions all follow a similar structure. The above picture is the function for updating a courier. Each record in my database tables have several aspects that make them unique. A user may want to update the entire record, or only some parts of it, so I added the option to skip updating values if they did not want to change them. This function:

1. Prints the relevant list so that the user can choose the correct record to update. 
2. Creates a variable that contains user input to specify the record they would like to update. 

This function relies on another, which takes the user input requested above and grabs the record from the table. 

![alt text](<get courier function.png>)

    3.1 This function specifies that it needs the courier_id as an argument in order to execute correctly. 
    3.2 It then uses SELECT to get the specified record WHERE the courier_id matches. 
    3.3 cursor.execute() runs the variable "print_<"object">_query" and uses the given argument as the id value. 
    3.4 cursor.fetchall() will return all the records that match the specifications and these will then be printed by the print statement. 

![alt text](<update courier yn.png>)

4. After the nested get function, the update function runs through several if statements for the relevant fields of the record. If the input is "y", then another nested function for the database will be executed. If not, then it will move to the next if statement until it has finished.

![alt text](<update db function.png>)

Here is an example of one of the nested functions that will take the user input and update the record field with the given value. 

5. Next, the code will commit the changes to the database and print out the updated list with the updated record included. 

### Deleting functions

![alt text](<remove function.png>)

Again, my delete function follows the same struture throughout all of my menus. The above picture is an example of the remove order function. It relies on two nested functions: "get_<"object">()" and delete_<"object">_record()". I have already explained the first one above, the second one has a similar structure:

![alt text](<delete record function.png>)

This function requires the id of the record being deleted in order to execute. It then uses DELETE FROM to specify the table and WHERE to identify the record to be deleted. This deletes the record from the table and commits the changes to the database and then the main function prints the updated list with the record removed. 


### Orders Menu

The orders menu is the most complex file I had to make because, in order to normalise my data, I had to have several tables that interacted with eachother to create an order. I have created a diagram to explain my table structure more clearly:

![alt text](<orders table structure.png>)

#### Adding an order

![alt text](<add order.png>)

The add order functions has a few extra steps than my other add functions:
1. It asks the user to confirm whether the order they want to add if for an existing customer or a new one. If it is for a new one then the query_customer() function takes them through adding a new customer to the database. 
2. It then goes through each part of adding a new order, printing the relevant list and asking the user to select the correct record by the ID. 
3. add_new_order() function takes this information and creates a new order in the orders table.
4. In order to normalise my data, I had to add an additional step: confirm the order they want to add items to and then using the add_orderline() function to add product items to the order. 

![alt text](<add orderline.png>)

![alt text](<add new orderline.png>)

The two functions pictured above allows a user to add multiple entries to the orderline table in the database. The first allows the user to add multiple entries to the table as if they were adding items to the order. The second handles adding the new orderline record to the orderline table, by adding new entries and storing them against the same order_id so that they can be searched later to see a full list of products ordered. 

## TESTING THE APP

As my app works with a database, I needed to use MagicMock and patch to mock the expected database responses in the functions. 

![alt text](<test database fixtures.png>)

I created fixtures, which is reusable logic for pytest to set up a testing environment for my imported functions. mock_db() creates a mock cursor and connection so that, when I am testing my functions, I don't accidentally affect the actual data stored in my real database. This means that the functions can be tested safely. patch_db() uses monkeypatch and my mock_db() function to temporarily replace my cursor and connection and the database connection with the test ones I have created. 

### Testing the get function 

![alt text](<test get product.png>)

This function is testing get_product() to see if it is taking in the correct input and outputting the correct information. This uses the mock_db fixture I created earlier and capsys, which captures the stdout (standard output) and stderr (standard error) being printed to the console. For the purpose of this test I didn't need the connection mock as I was not commiting anything back to the database, so I have used an underscore to get the function to ignore that part of my fixture and only use mock_cursor. 

mock_cursor.fetchall.return_value should return the values I have fed into it as a sample snippet of the database information. I gave it two test cases to see if it could correctly return the tuple I asked for. I also added a line to print the results as I was having errors when creating this code, so this is just a line to make sure it is grabbing the correct data and handling it properly. 

I then import my function from the module it is stored in and call it, with a given test value (in this case it is 1 as I want it to return the first test record I have given it.)

capsys.readouterr() captures both the standard output and any errors produced; I have stored this value in a variable so that I can add both attributes to my assertion. The assertion is declaring that the captured output will match ("1, 'test product 1', 9.99"), which is the first tuple I gave it to it earlir. If these do not match then the test will fail and return an assertion error. 

### Testing the add function

For the next function, I created a happy and unhappy test to see how it would handle both correct and incorrect inputs. 

![alt text](<test add new product happy.png>)

I had lots of issues getting this test to work as, although the function worked in practice, I could not get the test to fully pass becuase it wouldn't register that the commit had been called at least once. My solution was to explicitly patch the connection and cursor inside of the function, replacing these objects in my module temporarily with the mock versions. 

I also added in two print statements for the purpose of debugging. These used the call_count feature of Mock to print the number of times the cursor.execute and connection.commit were called. I gave the test some expected parameters for the SQL command (which I matched exactly to the actual function SQL query) and a test product to print (which I matched exactly to the parameters I added when I called the actual function).  I then used the call_args attribute to match the mock_cursor.execute to the actual parameters and SQL query. 

Next, I asserted that the expected parameters I declared earlier would match the actual parameters and if not then the test would fail and would print "SQL parameters mismatched". I then called the mock_cursor.execute with the expected SQL and parameters and used the assert_called_any to check if the execute was called at least once with these values. I also added .strip() in case the whitespace in the SQL query was causing the errors I was experiencing. I then used the assert_called_once attribute to check that the connection.commit was being called correctly. 


![alt text](<test add product unhappy.png>)

Next, I wanted to test the unhappy path of this function to see how it handled an incorrect input. I used the side_effect attribute to simulate what happens when the execute function fails to work. I gave it a failure message "database error" to print as the exception. 

Because I struggled with the first test of this function, I decided to explicitly patch the connection and cursor again within the function to avoid the errors I was getting earlier. I imported and called the function with these patches in place and gave it a test product to work with. 

I then used capsys again to capture the error message printed out and asserted that it would match my given error message "unable to add product". After this, I used the assert_not_called attribute with my mock_cursor.commit to check that the console would print out the correct message if incorrect information was passed. 

## PROJECT REFLECTIONS

### How did your design go about meeting the project's requirements? 

I started out working on each menu separately, one feature at a time to ensure that I could get my app to complete each requirement. I decided to start with laying out how the menus would look and then went down the menu list, adding each functionality as I went along. Printing the lists seemed like the best place to start, as that would give my other functions data to work on. The next logical step, in my mind, was to be able to add an item to these lists. After that, it made sense to be able to add the ability to update the information I had just added and then the last step would be to delete the record entirely. By building each feature this way, I could see clearly how they linked together. Once I had completed one menu, I could then use it as the framework to build the rest of the menus, as they all needed to do basically the same thing. 

### How did you guarantee the project's requirements? 

I tried to visualise how a user would want the app to function and what path they would need to take to get the desired output. With this in mind, I designed my menus and queries to clearly prompt the user to input the correct data and added in exceptions to tell the user what the error is and relooping them to the beginning to retry. 

I created a schema for my database so that I could understand how the data would be handled to meet 3NF requirements. I then used this to create my database and coded the functions to mirror these relationships. 

Throughout the process, I ran my code to test the functionality and clean up any errors that would prevent the user from moving forward. I then created some tests to make sure that the functions were communicating with the database correctly and handled the data how I expected it to. 

### If you had more time, what is one thing you would improve upon? 

I would like to be able to add in more of the bonus requirements for week 6 and to make my testing more robust. I didn't have time to add in a feature to track the inventory of my products or display orders by courier or status, although I can see how I could implement these if I had more time. As I was unfamiliar with how to test functions that relied on a database connection, I spent a lot of my time in the last week researching and trialling MagicMock and patch to try and mock the database feeatures. If I had more time, I would have tested more features of my app and given more cases to test the functionality. 

### What did you most enjoy implementing? 

I enjoyed implementing the database into my project, as I have had experience with databases in the past and I could already see early on how it would be much easier to run my app with a database rather than through lists or CSV files. It took a while to get the Docker connection to work and learn the correct syntax for adding records to a database but, once I had gotten past these issues, I really enjoyed it! 