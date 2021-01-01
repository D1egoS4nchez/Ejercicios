#!/usr/bin/env python3
#-*- coding: utf-8 -*-

"""
Confeccionar un programa que contenga las siguientes funciones:
1) Carga de una lista de 5 nombres.
2) Ordenar alfabéticamente la lista.
3) Imprimir la lista de nombres
"""

def cargar():
    nombres = []
    for x in range(5):
        nom = input("Ingrese el nombre: ")
        nombres.append(nom)
    return nombres

def ordenar(nombres):
    for k in range(4):
        for x in range(4):
            if nombres[x]>nombres[x+1]:
                aux = nombres[x]
                nombres[x] = nombres[x+1]
                nombres[x+1] = aux

def imprimri(nombres):
    for x in nombres:
        print(x," ",end="")


def main():
    nombres = cargar()
    ordenar(nombres)
    imprimri(nombres)

main()
