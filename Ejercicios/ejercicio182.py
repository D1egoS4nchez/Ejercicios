#!/usr/bin/env python3  
#-*- coding: utf-8 -*-
import random
"""
Confeccionar una programa con las siguientes funciones:
1) Generar una lista con 4 elementos enteros aleatorios comprendidos entre 1 y 3. Agregar un quinto elemento con un 1.
2) Controlar que el primer elemento de la lista sea un 1, en el caso que haya un 2 o 3 mezclar la lista y volver a controlar hasta que haya un 1.
3) Imprimir la lista.
"""

def generar():
    lista = []
    for x in range(4):
        valor = random.randint(1,3)
        lista.append(valor)
       
    lista.append(1)
    print(lista)
    return lista

def imprimir(lista):
    print(lista)
"""
def checar(lista):
    if lista[0] == 1:
        pass
    else:
        while lista[0] > 1:
            imprimir(lista)
            if lista[0] == 1 or lista[0] == 2 or lista[0] == 3:
                lista = random.shuffle(lista)
    print(lista)  
"""

def checar(lista):
    while lista[0]!=1:
        random.shuffle(lista)

    
lista = generar()
checar(lista)
imprimir(lista)
