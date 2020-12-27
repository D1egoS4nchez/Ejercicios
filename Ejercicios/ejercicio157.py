#!/usr/bin/env python3
#-*- coding: utf-8 -*-

""" Definir una función que cargue una lista con palabras y la retorne.
Luego otra función tiene que mostrar todas las palabras de la lista que tienen más de 5 caracteres. """

def numero():
    n = int(input("Cuantos valores quiere ingresar en la lista"))

    return n


def cargar():
    n = numero()
    liste = []
    for j in range(n):
        valor = input("Ingrese el valor: ")
        liste.append(valor)
    return liste


def otra(lista):
    cant = 0
    for valor in lista:
        if len(valor) >= 5:
            cant += 1
    return cant


#MAIN BLOCK

lis = cargar()
print("Hay {} palabras que son mayores a 5".format(otra(lis)))
