#Sumar los números en una lista:
#Dada una lista de números (por ejemplo, [1, 2, 3, 4, 5])
#usa un for para sumar todos los números e imprimir el resultado.

cadena=input("Ingrese 5 numeros: ")
cadena_separa = cadena.split()
suma = 0

for i in cadena_separa:
    suma = int(i) + suma
print(suma)