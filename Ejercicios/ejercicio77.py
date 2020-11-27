#!/usr/bin/env python3
# -*- coding: utf-8 -*-


#Almacenar en una lista los sueldos (valores float) de 5 operarios. Imprimir la lista y el promedio de sueldos.


lista_sueldo = []
suma = 0

for x in range(1,6):
    valor_ingresado = int(input("Ingrese el sueldo {}: ".format(x)))

    lista_sueldo.append(valor_ingresado)

    suma += valor_ingresado



print("La suma es ".format(suma))
promedio = suma / 5
print("La lista es {}".format(lista_sueldo))

print("Y el promedio es {}".format(promedio))
