num1 = int(input("Ingrese el numero hasta tres cifras"))

if num1 >= 1000: #Se coloca una condicion por si se ingresa un valor que no es correcto, si se coloca uno de 4000, la condicion termina ahi, ya que no se cumple.
	print("No se permiten numeros mayores a cuatros cifras,intente de nuevo")
else:
	if num1 >= 100: #Si se cumple funcion esta va a terminar aqui, diciendo que tiene 3 cifras
		print("Tiene tres cifras")

	else: #Si no se cumple la condicion, esta se para a la ultima condicion
		if num1 >= 10:
			print("Tiene dos cifras")
		else:
			print("TIene una cifra") 

