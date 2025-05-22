#Actividad: Gestión de inventarios con funciones y colecciones



inventory = {} # Diccionario, donde la clave es el nombre del producto
#y el valor es una tupla (precio, cantidad)

def addproduct(product, price, quantity):
    if product in inventory: #Verifica si el producto ya existe
        print("The product already exists")
    else:
        inventory[product] = (price, quantity) #Añade el producto al inventario
        print("The product has been ingresed correctly")

def searchproduct(searched):
    if searched in inventory:
        price, quantity = inventory[searched] #Obtiene el precio y la cantidad
        print(f"Product: {searched}\nPrice: ${price}\nQuantity: {quantity}")
    else:
        print("This product is not in the inventory")

def updateprice(updated):
    if updated in inventory:
        while True:
            try:
                new_price = float(input(f"Enter the new price for {updated}: "))
                if new_price < 1: #verifico que sea un valor positivo
                    print("The price must be greater than 0.")
                else:
                    break
            except ValueError: #si no es un valor numerico arroja error
                print("Enter a valid numeric price.")
        current_quantity = inventory[updated][1] #Obtiene la cantidad actual del producto
        inventory[updated] = (new_price, current_quantity) #Actualiza el precio en el inventario
        print(f"The price for '{updated}' has been updated to ${new_price}")
    else:
        print("The product is not in the inventory")    
        
def deleteproduct(deleted):
    if deleted in inventory: #verifica si existe en inventario
            del inventory[deleted] #si existe lo elimina
            print(f"The product '{deleted}' has been removed from the inventory.")
    
    else:
        print("That product does not exist in the inventory.")

def total_inventory_value():
    total_value = 0 #inicializa el valor total en 0
    for product in inventory.values(): #recorre los productos en inventario y trae valores
        total_value += (lambda price, quantity: price * quantity)(product[0], product[1]) #calcula el valor de cada producto
    print(f"The total value of the inventory is: ${total_value:.2f}")#muestra el valor con 2 decimales
        

def showmenu(): #funcion menu para interactuar
    while True:
        menu_option = int(input("Welcome to Shop-Solution\nChoose an option: \n" \
        " 1. Add product\n 2. Search product\n 3. Update prices\n 4. Delete product\n 5. Calculate total inventory value\n->"))
        if menu_option < 1 or menu_option > 5:
            print("Choose a number between 1 and 5") #verifica que la opcion sea entre 1 y 5
        else:
            match menu_option:
                case 1:
                    product = str(input("Enter the product's name: ")).lower()
                    while True:
                        try:
                            price = float(input("Enter the product's price: "))
                            if price < 1:
                                print("The value has to be a positive number or greater than 1")
                            else:
                                break
                        except ValueError:
                            print("Enter a valid numeric price")
                    while True:
                        try:
                            quantity = int(input("Enter the product's available quantity: "))
                            if quantity < 1:
                                print("The value has to be a positive number or greater than 1")
                            else:
                                break
                        except ValueError:
                            print("Enter a valid number")
                    addproduct(product, price, quantity)

                case 2:
                    
                        searched = input("Enter the product that you are looking for: ").strip().lower()#con el strip elimino espacios para evitar errores al llamar productos
                        
                        if searched == "":
                            print("Product name cannot be empty.")
                        else:
                            searchproduct(searched)
                case 3:
                    updated = input("Enter the product to update its price: ").lower()
                    updateprice(updated)

                case 4:
                    deleted = input("Enter the product to delete: ").lower()
                    deleteproduct(deleted)

                case 5:
                    total_inventory_value()

showmenu()