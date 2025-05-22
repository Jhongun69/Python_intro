#Prueba de desempeño – Módulo 1

inventory = [
    {"product": "mango", "price": 2000.0, "quantity": 100}, 
    {"product": "manzana", "price": 800.0, "quantity": 50},
    {"product": "doritos", "price": 2500.0, "quantity": 30},
    {"product": "chocorramo", "price": 2300.0, "quantity": 10},
    {"product": "gaseosa", "price": 6000.0, "quantity": 5}
]


def add_product(product, price, quantity): #create the add product function
    new_product = {"product": product,"price": price,"quantity": quantity}#a new variable is started and user data is assigned to it
    inventory.append(new_product)#use .append to add the product(new variable) to our dictionary
    print("The product has been ingresed correctly")
#---------------------------------------------------------------------------------------------------
def search_product(searched):#create the seFarch function
    found = False #variable is initialized as false by default
    for products in inventory:
        if products['product'].lower() == searched: #check if the product is in the dictionary
            print(f"Product: {products['product']}\nPrice: ${products['price']}\nQuantity: {products['quantity']}")#we use the product as key to access the dictionary values
            found=True #When the item is found in the dictionary, the variable becomes true.
            break
    if not found:
        print("This product is not in the inventory")#if the item is not in the inventory the variable still false and print a message
#---------------------------------------------------------------------------------------------------
def update_price(updated): #create the price change function
        for products in inventory:
            try:
                if products['product'].lower() == updated.lower():#check if the product is in the dictionary
                    print("The product has been found it")
                    
                    newprice = float(input("Enter the price to update: $"))#ask for a new price
                    if newprice > 0:#check if it is a positive number
                        products["price"]=newprice #a new value is assigned to "product"
                        print("The price has been updated")  
                    else:
                       print("The value has to be a positive number or greater than 1")
                    return 
            except ValueError: #check if it is a valid number
                    print("Enter a valid number")
        else:
            print("The product isn't in the inventory")
             
#---------------------------------------------------------------------------------------------------
def delete_product(deleted): #create delete function
    for products in inventory:
        if products["product"].lower() == deleted.lower():#check if the product is in the dictionary
            print("The product is in the inventory")
            confirmation = input("Do you want to delete this product? (yes/no): ")#ask for a confirmation
            if confirmation.lower()=="yes":
                inventory.remove(products) #delete the product from the dictionary
                print(f"The product {products['product']} has been deleted successfully")
                return
            else:
                print("product not deleted")#if the user doesn't confirm the product is not deleted
                return
    else:
        print("the product doesnt exist in inventory")
#---------------------------------------------------------------------------------------------------

def total_inv_value(): #create total inventory value function
    total = 0 #start the variable in 0
    for products in inventory:
        total += products["price"]*products["quantity"] #It goes through the entire dictionary and multiplies prices by quantity, then adds the total.
    return total
    
    
#---------------------------------------------------------------------------------------------------
def showmenu(): #create the menu to interact
    while True:
        print("Welcome to Inventory Plus")
        menu_option = int(input("Choose your option:\n 1. Add products\n 2. Search product\n 3. Update product price\n 4. Delete products\n 5. Calculate total inventory value\n-> "))
        if menu_option < 0 or menu_option > 5: #check if the number is between 1 and 5
            print("Please choose a correct option")
        else:
            match menu_option: #select an option based on the user's response
                case 1:
                    product = str(input("Enter the product's name: ")).lower()

                    while True:
                        try:
                            price = float(input("Enter the product's price: $"))
                            if price < 1: #check if the price its a positive number
                                print("The price has to be a positive number or greater than 1")
                            else:
                                break
                        except ValueError:#check if it is a valid number
                            print("Enter a valid numeric price")
                    while True:
                        try:
                            quantity = int(input("Enter the product's available quantity: "))
                            if quantity < 1:# check if the price its a positive number
                                print("The quantity has to be a positive number or greater than 1")
                            else:
                                break
                        except ValueError:#check if it is a valid number
                            print("Enter a valid number")
                    add_product(product, price, quantity)#the function its called
                case 2:
                    searched = str(input("Enter the product that you are looking for: ")).lower()
                    search_product(searched)#the function its called
                case 3:
                    updated = str(input("Enter a product to update its price: "))
                    update_price(updated)#the function its called
                case 4:
                    deleted = str(input("Enter a product to delete: "))
                    delete_product(deleted)#the function its called
                case 5:
                    print(f"The total inventory value is: ${round(total_inv_value(),2)}")#the function its called and print with 2 decimals
                   

showmenu()#the function its called
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#ReadMe
# Initially, what the inventory operations leader requests is analyzed and, according to his needs, the code is executed.

# 1. A function is created to show the interaction menu to the user where they can choose the options to execute the program.

# 2. Once the options that the user will have are defined, the specific functions of each option are created.

# 3. The function to add products to the inventory is created, where it requests the product name, price and available quantity.
# Validations are performed to ensure the user enters data correctly. In the function, the data entered by the user is assigned to a new variable., which is 
# stored in our list (inventory), this create a new product in the list.

# 4. The function to search for products is created, where the user is asked for a product to search for, The program checks whether the product is listed, and if so, 
# it prints the stored values ​​such as product, price, and quantity. If the product is not listed, it prints a message to the user.

# 5. The function to update product prices is created. The program verifies that the entered product is on the list. 
# If it is, a new value (price) is requested and its entry is validated. If it is correct, the new price is assigned to the product and the user is notified.

# 6. The function to delete products is created, it is verified that the product exists and the user is notified, 
# the deletion of the product is confirmed with the user and it is removed from the list, in case the product does not exist the user is notifie

# 7. The function is created to calculate the total value of the inventory where a variable (total) is started with zeros, 
# then the values ​​(price and quantity) of each key (product) are multiplied and then added together, being assigned to the variable started with zeros (total) 
# then the total value of their inventory is shown to the user.

