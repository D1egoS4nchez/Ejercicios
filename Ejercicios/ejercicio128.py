#!/usr/bin/env python3
#-*- coding: utf-8 -*-

""" Crear y cargar por teclado en el bloque principal del programa una lista de 5 enteros.+
Implementar una función que imprima el mayor y el menor valor de la lista. """

def mayormenor(lista):
    may = lista[0]
    men = lista[0]
    for x in range(len(lista)):
        if lista[x]>may:
            may = lista[x]
        else:
            if lista[x]<men:
               men = lista[x]
    print("El valor mayor de la lista {}".format(may))
    print("El valor menor de la lista es {}".format(men))


# Bloque principal

lista = []

for x in range(5):
    valor = int(input("Ingrese el valor numero {}: ".format(x)))
    lista.append(valor)

print(lista)

mayormenor(lista)
