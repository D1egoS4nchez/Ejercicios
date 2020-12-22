#!/usr/bin/env python3
#-*- coding: utf-8 -*-

"""Confeccionar una función que reciba una serie de edades y me retorne la cantidad que 
son mayores o iguales a 18 (como mínimo se envía un entero a la función)"""

def cantidad_mayores(edad1, *edades):
    cantidad = 0
    if edad1>18:
        cantidad += 1
    for x in range(len(edades)):
        if edades[x] >= 18: 
            cantidad += 1
    return cantidad



print("La cantidad de personas que son mayores de edad son  {}".format(cantidad_mayores(23,17,6,19,16)))
