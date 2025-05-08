#Actividad: Desafío de calificaciones y estadísticas
while True:
    calificacion = int(input("Ingresa una calificacion de 0-100: "))  #solicitar información al usuario
    if calificacion < 0 or calificacion > 100:                        #verificar que cumpla el rango
        print("La calificacion debe estar entre 0 y 100")
    else:
        if calificacion >= 60:
            print("Has aprobado")
        else:
            print("Has reprobado")

    print("Ahora vamos a evaluar tu lista de calificaciones")        #lista de calificaciones
    cadenanotas = input("Ingresa tus calificaciones separadas por comas: \n") #solicita info al usuario
    cadenatexto = cadenanotas.split(",")                          #separamos el texto en varios strings
    cadenanumeros = []                       #se crea variable para guardar el texto convertido a numero

    for texto in cadenatexto:
        num = int(texto)
        cadenanumeros.append(num)                      #se convierte cada texto a numero y se almacena

    suma = 0
    for num in cadenanumeros:
        suma += num                                     #se suma cada numero y se asigna a la variable
    promedio = suma / len(cadenanumeros)                #calculo del promedio
    print("El promedio de tus calificaciones es:",promedio)
    if promedio >= 60:
        print("Has aprobado")
    else:
        print("Has reprobado")

    valorcomparar = int(input("Ingresa un valor para comparar: \n"))          #solicita info al usuario
    contador = 0                   #se inicia un contador para sumar cuantas notas cumplen la condicion
    i = 0                                    #variable para recorrer la lista y acceder a sus elementos

    while i < len(cadenanumeros):
        if cadenanumeros[i] > valorcomparar: #si el numero en n posicion de la cadena es mayor se suma el contador
            contador = contador + 1
        i = i + 1
    print("Hay",contador,"calificaciones mayores que",valorcomparar) 

    buscar = int(input("Ingresa la calificacion que quiere buscar: "))
    contador1 = 0

    for nota in cadenanumeros:
        if nota < 0 or nota > 100:
            continue
        if nota == buscar:
            contador1 = contador1 + 1
        if contador1 > 10:
            print("La nota aparece muchas veces, deteniendo busqueda")
            break
    print(f"la calificacion {buscar} aparece {contador1} veces")

    salir = input("Deseas salir? (Si/No) -").lower()
    if salir == "si":
        print("Saliendo...")
        break
