#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Definir una lista por asignación con 5 enteros. Mostrar por pantalla solo los elementos con valor iguales o superiores a 7."""


lista_ocho_valores = [23,6,21,4,12]

contador = 0
for x in range(len(lista_ocho_valores)):
    if lista_ocho_valores[x] >= 7:
        contador += 1
    else:
        print("No pa, el numero {} no es mas grande que 7".format(lista_ocho_valores[x]))

print("Hay {} numeros mas altos que 7".format(contador))
