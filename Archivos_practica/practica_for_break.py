numeros = [9,15,36,98,99,80]
umbral =40

for numero in numeros:
    if numero > umbral:
        print(f"EL primer numero mayor que {umbral} es {numero}")
        break
else:
    print("Ningun numero en la lista es mayo que",umbral)
#aqui el break detiene la condicion para que solo se evalue una vez
#si no esta el break se evalua las veces necesarias hasta que se cumpla