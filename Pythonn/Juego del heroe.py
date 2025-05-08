#Juego del heroe
vidaheroe=100
print("Bienvenido a virtual hero\n\n\n")
heroe1 = int(input("¡Escoge tu héroe!\n\n 1.Flamecat / 2.Dogodrile -\n"))
print("-" * 25)
if heroe1 == 1:
    print(f"Has seleccionado a Flamecat\n\n " \
    "Es un felino agil con poderes de fuego")
else: 
    heroe1 == 2
    print("Has seleccionado a Dogodrile")
    print("Es una fusión fuerte con una mandibula poderosa")
print()
print("Estas caminando y el camino se divide en dos")
camino1=input("izquierda o derecha? -").lower()
if camino1 == "izquierda":
    print("Ingresaste a una cueva oscura")
    luz=input("Esta muy oscuro, tienes fuego?(Si/No) -").lower()
    if heroe1 == 1 and luz == "si":
        print("Muy bien, has iluminado la cueva con tu poder de fuego")
    elif heroe1 == 2 and luz == "si":
        print("No tienes poderes de fuego (puedes perder salud en lugares oscuros)")
    elif heroe1 == 1 and luz == "no":
        print("Claro que tienes fuego, eres flamecat, has illuminado la cueva")
    elif heroe1 == 2 and luz == "no":
        print("Continuas en la oscuridad(puedes perder salud ocasionalmente)")
    vidatopo=100
    print("Estas caminando y aparece un topo salvaje")
    if luz == ("si") or ("no") and heroe1 == 1:
        print("Al tener iluminada la cueva atacas primero")
        ataque1=input("Elige tu ataque: Maullido o Garrafuego -").lower()
        if ataque1 == "garrafuego":
            print("Flamecat golpea a Topo salvaje")
            vidatopo = vidatopo -50
            print("Salud del topo se reduce a:"),print(vidatopo)
        elif ataque1 == "maullido":
            print("Ya tienes la salud al maximo")
            

else:
    camino1 == "derecha"
    print("Ingresaste a la jungla")
