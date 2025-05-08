#3. Extraer hora, minuto y segundo de segundos totales
#Pide al usuario un número de segundos y muestra cuántas horas, minutos y segundos son.
#📌 Ejemplo: 3665 segundos → 1 hora, 1 minuto, 5 segundos.

seg_inicial=int(input("Ingrese una cantidad de segundos "))

hora=seg_inicial//3600
minuto=(seg_inicial%3600)//60
segundo=seg_inicial%60

print(seg_inicial,"segundos son",hora,"horas y",minuto,"minutos y",segundo,"segundos")