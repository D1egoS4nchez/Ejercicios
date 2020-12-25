#!/usr/bin/env python3  
#-*- coding: utf-8 -*-

""" 
Almacenar en una lista de 5 elementos tuplas que guarden el nombre de un pais y la cantidad de habitantes.
Definir tres funciones, en la primera cargar la lista, en la segunda imprimirla y en la tercera 
mostrar el nombre del país con mayor cantidad de habitantes.
"""


def cargar_paisespoblacion():
    paises = []
    for x in range(5):
        nom = input("Ingrese el nombre del pais: ")
        cant = int(input("Ingrese la cantidad de habitantes: "))
        paises.append((nom,cant))
    return paises

def imprimir(paises):
    print("Paises y poblacion")
    for x in range(len(paises)):
        print(paises[x][0], paises[x][1])

def pais_mas(paises):
    pos = 0
    for x in range(1, len(paises)):
        if paises[x][1]>paises[pos][1]:
            pos=x
    print("Pais con mayor cantidad de habitantes:",paises[pos][0])

#MAIN BLOCK

paises = cargar_paisespoblacion()
imprimir(paises)
pais_mas(paises)
