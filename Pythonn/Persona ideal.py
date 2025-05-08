#Persona ideal

puntaje=0

pregunta1=input("Eres mujer? ")
if pregunta1 == "si":
    puntaje = puntaje + 10

    pregunta2=input("Eres mayor de edad? ")
    if pregunta2 == "si":
        puntaje = puntaje + 10
    else:
        puntaje = puntaje - 100

    pregunta3=input("Eres timida? ")
    if pregunta3 == "si":
        pregunta4 =int(input("Que tan timida eres del 1 al 10? "))
        if pregunta4 >=1 and pregunta4 <=3:
            puntaje = puntaje + 10
        elif pregunta4 >=4 and pregunta4 <=7:
            puntaje = puntaje + 5
        elif pregunta4 >=8 and pregunta4 <=10:
            puntaje = puntaje + 1

    else:
        pregunta3 == "no"
        puntaje = puntaje + 10

    pregunta5 =input("Eres tierna? ")
    if pregunta5 == "si":
        puntaje = puntaje + 10
    else:
        puntaje = puntaje - 10

    pregunta6 =input("Te gustan las motos? ")
    if pregunta6 == "si":
        puntaje = puntaje + 10
        if pregunta6 == "si":
            pregunta7 =input("Puedes mencionar 5 marcas de motos? ")
            if pregunta7 == "si":
                puntaje = puntaje + 10
        

    else:
        puntaje = puntaje - 10

    pregunta8 =input("Tienes claro lo que quieres hacer con tu vida? ")
    if pregunta8 == "si":
        puntaje = puntaje + 10
    else:
        puntaje = puntaje - 10

    pregunta9 =input("te puedes parchar con cualquier tipo de música? ")
    if pregunta9 == "si":
        puntaje = puntaje +10
    else:
        puntaje = puntaje -10

    pregunta10 =int(input("del 1 al 10 que tan malgeniada eres? "))
    if pregunta10 >=1 and pregunta10 <=3:
        puntaje = puntaje + 10
    elif pregunta10 >=4 and pregunta10 <=7:
        puntaje = puntaje + 5
    elif pregunta10 >=8 and pregunta10 <=10:
        puntaje = puntaje + 1

    pregunta11 =input("te gustan las mascotas? ")
    if pregunta11 == "si":
        puntaje = puntaje + 10
    else:
        puntaje = puntaje - 10
    
else:
    print("No puedes continuar :)")


print("Tu puntaje total fue:",puntaje)
if puntaje == 110:
    print("wow, Eres perfecta, 10/10")
elif puntaje <= 109 and puntaje >= 90:
    print("Podemos conocernos...")
elif puntaje <= 89 and puntaje >= 70:
    print("Podemos ser amigos :)")
elif puntaje <= 69 and puntaje >= 40:
    print("Que Dios te bendiga jaja")
elif puntaje <=39 and puntaje >= 20:
    print("Deje así mas bien")
elif puntaje <= 19:
    print("nada que hacer con usted")