num1 = int(input("Ingrese el numero hasta tres cifras"))

if num1 >= 1000:
	print("No se permiten numeros mayores a cuatros cifras,intente de nuevo")
else:
	if num1 >= 100:
		print("Tiene tres cifras")

	else:
		if num1 >= 10:
			print("Tiene dos cifras")
		else:
			print("TIene una cifra") 

