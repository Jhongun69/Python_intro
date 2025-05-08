#6. Cálculo de propina y cuenta total Pide el costo de una comida y calcula el 10%, 15% y 20% de propina. Muestra el total a pagar en cada caso.

factura=float(input("Ingrese el valor total de su factura "))
propina=float(input("Ingrese el porcentaje de su propina "))

if propina < 0 or propina > 100:
    print("El valor de la propina debe estar entre 0 y 100")
else:    
    propinatotal=(propina / 100)*factura
    facturatotal=factura+propinatotal

    print("El valor de la propina es de",propinatotal)
    print("el valor a pagar con",propina,"% de propina es",facturatotal)
