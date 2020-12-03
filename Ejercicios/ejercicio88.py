#!/usr/bin/env python3
# -*- coding: utf-8 -*-


sueldos = []

for x in range(5):
    valor = int(input("Ingrese el sueldo"))
    sueldos.append(valor)

print("Lista sin ordenar \n {}".format(sueldos))
#Con este for se repite el bucle 4 veces seria en total 16 vueltas para checar y acomodar por que esto es igual a esto:
"""
Cuando k = 0
		x = 0		x = 1		x = 2		x = 3
		750		    750		      750		     750
		1200		820		820		             820
		820		    1200		550		          550
		550		    550		      1200	        490
		490		    490		      490		      1200

Cuando k = 1
		x = 0		x = 1		x = 2		x = 3
		750		    750		      750		750
		820		    550		      550		550
		550		    820		      490		490
		490		    490		      820		820
		1200		1200		1200		1200

Cuando k = 2
		x = 0		x = 1		x  = 2		x = 3
		550		    550		      550		      550
		750		    490		      490		      490
		490		    750		      750		      750
		820		    820		      820		      820
		1200		1200		     1200		1200


Cuando k = 3
		x = 0		x = 1		x  = 2		x = 3
		490		    490		      490		      490
		550		    550		      550		      550
		750		    750		      750		      750
		820		    820		      820		      820
		1200		1200		1    200		1200
"""

for x in range(4):
    #Solo para saber cual es el más grande tenemos que mover la secuencia 4 veces
    for x in range(4):
        if sueldos[x]>sueldos[x+1]:
            #Se guarda una variable auxiliar para guardar el valor de la lista de la posicion x
            aux = sueldos[x]
            #Se modifica la posicion x por la x + 1 que es el siguiente valor ya que es menor sueldo[x+1] a sueldo[x] entonces se cambia la posicion
            sueldos[x] = sueldos[x+1]
            #Se cambia la posicion de la que antes era x+1 con el valor anterior que se guardo en la variable auxiliar que tiene el valor de la vuelta y como se cumplio la condicion este es mayor
            sueldos[x+1] = aux
print("Lista con el último elemento ordenado")
print(sueldos)
