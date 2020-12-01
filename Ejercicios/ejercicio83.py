#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Cargar una lista con 5 elementos enteros. Imprimir el mayor y un mensaje si se repite dentro de la lista (es decir si dicho valor se encuentra en 2 o más posiciones en la lista)"""


lista = []

for x in range(5):
    valor = int(input("Ingrese el {} elemento: ".format(x)))
    lista.append(valor)

mayor = lista[0]
contador_menor = 0
for x in range(5):
    if lista[x] > mayor:
        mayor = lista[x]
        posicion = x
    else:
        contador_menor = lista[x]

    

print("El numero mayor es {} y esta en la posicion de la lista numero {}".format(mayor,posicion))
