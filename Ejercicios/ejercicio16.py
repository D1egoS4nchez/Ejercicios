numero = int(input("Ingrese el numero: "))

if numero == 0: 	#Se comprueba que el numero sea 0
	print("El numero es nulo")

else: #Si este no es cero, se pasa a la siguiente funcion

	if numero >= 0: #Se ejecuta la condicion base
		print("El numero es positivo")

	else: #Si la condicion de arriba no se cumple, este sacará que es negativo
		print("El numero es negativo")
