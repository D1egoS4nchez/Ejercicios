#!/usr/bin/env python3
# -*- coding: utf-8 -*-


""" Cargar una oración por teclado. Mostrar luego cuantos espacios en blanco se ingresaron. Tener en cuenta que un espacio en blanco es igual a
" ", en cambio una cadena vacía es "" """

oracion = input("Ingrese una oracion para calcular cuantos espacios en blanco hay: \n")
x = 0
contador = 0
while x < len(oracion):
    z = 0
    if oracion[x] ==" ":
        contador = contador + 1

    x += 1
print("En la oracion hay {} espacios en blanco".format(contador))
