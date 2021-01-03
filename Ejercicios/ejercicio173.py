#!/usr/bin/env python3  
#-*- coding: utf-8 -*- 

"""
Realizar un programa que contenga las siguientes funciones:
1) Carga de una lista de 10 enteros.
2) Recibir una lista y retornar otra con la primer mitad (se sabe que siempre llega una lista con una cantidad par de elementos)
3) Imprimir una lista.
"""

def cargar():
    lista = []
    for x in range(1,11):
        valor = int(input("Ingrese el valor numero {}: ".format(x)))
        lista.append(valor)
    return lista


def mitad(lista):
    change = lista[:5]
    return change

#MAIN BLOCK

lista = cargar()
cambio = mitad(lista)
print(cambio(lista))


