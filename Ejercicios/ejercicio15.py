""" Se cargan por telcado tres numeros distintos. MOStrar por pantalla el mayor de ellos """


num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segudo numero: "))
num3 = int(input("Ingerse el tercer numero: "))
"""
if num1>num2 & num1>num3:
	print("El numero mayor es el uno : " + num1)

else:
	if num2>num1 & num2>num3:

		print("El numero mayor es el dos :" + num2)

	else:
		
		print("El numero tres es el mayor") """
"""
if num1>num2:
	if num1>num3:
		print("El numero uno es el mas grade")
	else:
		if num2>num1:
			if num2>num3:
				print("El numero dos es el numero mas grande")
			
			else:
				if num3>num1:
					if num3>num2:
						print("El numero tres es el numero mayor")
						print(num3)
"""

if num1>num2:  #Se hace la primera condicion, si esta no pasa, no se puede ir a chechar a la segunda condicion
	if num1>num3:  #Ya que se cumplio la condicion anterior, esta se tiene que cumplir para imprimir el numero
		print(num1)
	else: 
		print(num3)	#Si la segunda condicion no se cumple se va a ir al esle, ya teniendo en cuenta de que la primera condicion se cumplio y teniendo en cuenta de que la segunda condicion no se cumplio es porque el numero es mas grande que 1 y mas que 2

else:  #Si el primer bloque de condicion no se cumple, pasara al siguiente que estaria comparando al numero 2
	if num2>num3:
		 print(num2)

	else: 
		if num2<num3:		
			print(num3)
