#!/usr/bin/env python3
# -*- coding: utf-8 -*-


""" Definir una lista que almacene 5 enteros. Sumar todos sus elementos y mostrar dicha suma. """

lista = [10,7,3,7,2]

suma = 0
x = 0

while x <len(lista):
    suma += lista[x]

    x += 1

print("La suma de todos los elementos de la lista son {}".format(suma))
