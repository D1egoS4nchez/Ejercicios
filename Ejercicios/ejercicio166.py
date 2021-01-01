#!/usr/bin/env python3
#-*- coding: utf-8 -*-

"""
Confeccionar un programa que contenga las siguientes funciones:
1) Carga de una lista y retorno al bloque principal.
2) Fijar en cero todos los elementos de la lista que tengan un valor menor a 10.
3) Imprimir la lista
"""


def cargar():
    lista = []
    continua = "s"
    while continua == "s":
        valor = int(input("Ingrese un valor; "))
        lista.append(valor)
        continua = input("Agrega otro elemento [s/n]: ")
    return lista


def fijar(lista):
    for k in lista:
        if k < 10:
            k = 0

def imprimir(lista):
    for elemento in lista:
        print(elemento,"-",sep="",end="")
    print("")

# bloque principal

lista=cargar()
print("Lista antes de modificar")
imprimir(lista)
fijar(lista)
print("Lista despues de modificar")
imprimir(lista)
