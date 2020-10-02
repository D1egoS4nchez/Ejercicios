# Ejercicio numero 13 sobre estructuras condicionales simples y compuestas

nota1 = int(input("Ingrese la primer nota: "))
nota2 = int(input("Ingrese la segunda nota: "))
nota3 = int(input("Ingrese la tercera nota: "))

promedio = (nota1 + nota2 + nota3) / 3

if promedio>=7:                   #Se coloca la primera condicion
	print("Promocionado")

else: # Se usa el el else para irse a la otra condicion
	if promedio>=4: #Se pone la segunda condicion if
		print("Regular")

	else:   # Aqui se puede poner otra condicion
		print("Reprobado")


