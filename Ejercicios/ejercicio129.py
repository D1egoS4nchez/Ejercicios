#!/usr/bin/env python3
#-*- coding: utf-8 -*-


"""Crear una lista de enteros por asignación. Definir una función que reciba una lista de enteros y un segundo parámetro de tipo entero. 
Dentro de la función mostrar cada elemento de la lista multiplicado por el valor entero enviado. """

def lista_asignacion(lista, entero):
    for x in range(len(lista)):
        print(str(lista[x] * entero) + " ")




# BLOQUE PRINCIPAL
lista = [3, 7, 8, 10, 2]
lista_asignacion(lista, 3)
