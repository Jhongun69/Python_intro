#Calculadora de productos con posible descuento

print("Bienvenido a Costos Plus") #mensaje de bienvenida

nombreproducto = str(input("Ingresa el nombre del producto: ")) #variables con valores segun el usuario
precio = float(input("Ingrese el precio del producto: $"))
cantidad = int(input("Ingrese la cantidad adquirida: "))
dcto_porcentual = float( input("Ingrese el descuento en porcentaje (si aplica): "))

if 0 <= dcto_porcentual <= 100: #validacion para que el porcentaje de descuento esté entre 0 y 100

    ct = precio*cantidad #calculo del costo total

    if dcto_porcentual == 0: #calculo para determinar si el descuento fue 0
        print("El producto no tiene descuento") #mensaje en caso de que no tenga descuento el producto
        print("Producto:",nombreproducto,"El costo total de los productos es de: $",ct) #mensaje de costo total
    else:

   
     dcto = (ct*dcto_porcentual)/100 #calculo del descuento aplicado

     print(f"Producto:{nombreproducto}. El costo total de los productos es de: ${ct:.2f}") #mensaje costo total en caso que haya descuento
     print(f"Producto:{nombreproducto}. El costo total con descuento es de: ${ct-dcto:.2f}")#mensaje costo total con descuento 
     print("El descuento aplicado fue de: $",dcto) #mensaje del descuento aplicado

else:
    print("El porcentaje debe estar entre 0 y 100") #mensaje en caso de que se ponga un descuento fuera del rango permitido