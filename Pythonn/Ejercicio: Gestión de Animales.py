#Ejercicio: Gestión de Animales
#Desarrolla un programa en Python que permita gestionar información sobre animales. 
#El programa debe tener un menú usando funciones con las siguientes opciones: 
#recuerda que pasa nombre, edad y enfermo cada uno debe de guardarse en su propia lista
nombres=[]
edades=[]
enfermos=[] #se crean listas para guardar los datos de los animales
def showmenu(): #se crea la funcion del menu principal
    print("Bienvenido a Animals_Pro")
    print("1. Agregar un animal")
    print("2. Eliminar un animal")
    print("3. Listar todos los registros")
    print("4. Salir")

def agganimal(): #se crea la funcion para agregar animales
    nombre = input("Ingresa nombre del animal: ").lower()
    edad = input("Ingresa la edad del animal(años): ")
    enfermo = input("El animal esta enfermo?(si/no): ").lower()

    nombres.append(nombre)
    edades.append(edad)
    enfermos.append(enfermo == "si") #se añaden los datos a las listas

def eliminaranimal(): #se crea la funcion para eliminar animales
    nombre = input("Nombre del animal a eliminar: ")
    if nombre in nombres: #verificamos que el nombre exista en la lista
        i = nombres.index(nombre) #Busca en qué posición está ese nombre en la lista nombres y lo guarda en la variable i.
        nombres.pop(i)
        edades.pop(i)
        enfermos.pop(i) #se eliminan los datos del animal
        print(f"{nombre} fue eliminado.")
    else:
        print(f"{nombre} no está registrado.")

def listaranimales():
    if not nombres:
        print("No hay registros disponibles")
    else:
        for i in range(len(nombres)):
            estado = "Enfermo" if enfermos[i] else "Sano"
            print(f"{i + 1}. Nombre: {nombres[i]} - Edad: {edades[i]} años - {estado}")
while True:
    showmenu()
    opcion = input("Elige una opcion: ")
    if opcion == "1":
        agganimal()
    elif opcion == "2":
        eliminaranimal()
    elif opcion == "3":
        listaranimales()
    elif opcion == "4":
        print("Saliendo del programa....")
        break
    else:
        print("Opción no válida.")
