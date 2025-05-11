#Simulacro de Examen

inventory = [
    {"title": "Book 1", "price": 10.0, "quantity": 100},
    {"title": "Book 2", "price": 15.0, "quantity": 50},
    {"title": "Book 3", "price": 20.0, "quantity": 30},
    {"title": "Book 4", "price": 25.0, "quantity": 10},
    {"title": "Book 5", "price": 30.0, "quantity": 5}
]

def addbook(title, price, quiantity):
    newbook = {"title": title,"price": price,"quantity": quiantity}
    inventory.append(newbook)
    print("The book has been ingresed correctly")
#----------------------------------------------------------------
def searchbook(searched):
    found = False
    for book in inventory:
        if book['title'].lower() == searched:
            print(f"Book: {book['title']} Price: {book['price']} Quantity: {book['quantity']}")
            found=True
            break
    if not found:
        print("This book is not in the inventory")
#-----------------------------------------------------------------
def update_price(modified):
    while True:
        for book in inventory:
            try:
                if book['title'].lower() == modified.lower():
                    print("The book has been found it")
                    newprice = float(input("Enter the price to update"))
                    if newprice > 0:
                        book["price"]=newprice
                        print("The price has been updated")  
                    else:
                        print("The value has to be a positive number or greater than 1")
                     
            except ValueError:
                    print("Enter a valid number")
        else:
            print("The book isn't found in the inventory")   
            break           
#-----------------------------------------------------------------    

def delet_book():
    while True:
        for book in inventory:
            if book['title'].lower() == deleted.lower()

#-----------------------------------------------------------------
def showmenu():
    while True:
        print("Welcome to BookMaster")
        menuoption = int(input("Choose your option:\n " \
        "1. Add new book\n 2. Search book\n " \
        "3. Update book prices\n 4. Delete books\n " \
        "5. Calculate total inventory value\n"))
        if menuoption < 1 or menuoption > 5:
            print("Choose a correct option")
        else:
            match menuoption:
                case 1:
                    title = str(input("Enter the book's title: ")).lower()
                    while True:
                        try:
                            price = float(input("Enter the book's price: "))
                            if price < 1:
                                print("The value has to be a positive number or greater than 1")
                            else:
                                break
                        except ValueError:
                            print("Enter a valid numeric price")
                    while True:
                        try:
                            quantity = int(input("Enter the book's available quantity: "))
                            if quantity < 1:
                                print("The value has to be a positive number or greater than 1")
                            else:
                                break
                        except ValueError:
                            print("Enter a valid number")
                    addbook(title, price, quantity)
                case 2:
                    searched = str(input("Enter the title of the book that you are looking for: ")).lower()
                    searchbook(searched)
                case 3:
                    modified = str(input("Enter the title book to modify the price: ")).lower()
                    update_price(modified)
                case 4:
                    deleted = str(input("Enter the book to delete")).lower()
                    delet_book()


showmenu()