#!/usr/bin/env python3
#-*- coding: utf-8 -*-

""" Confeccionar una función que cargue por teclado una lista de 5 enteros y la retorne. 
Una segunda función debe recibir una lista y retornar el mayor y el menor valor de la lista. 
Desde el bloque principal del programa llamar a ambas funciones e imprimir el mayor y el menor de la lista. """

def cargar_lista():
    li = []
    for x in range(5):
        valor = int(input("Ingrese el valor: "))
        li.append(valor)
    return li




def retornar_mayor_menor(li):
    ma = li[0]
    me = li[0]
    for x in range(1,len(li)):
        if li[x]>ma:
            ma = li[x]
        else:
            if li[x] < me:
                me = li[x]
    return [ma,me]

#MAIN BLOCK Se escucha mas fresa en ingles

lista = cargar_lista()
print(lista)
retornar_mayor_menor(lista)


