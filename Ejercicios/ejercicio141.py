#!/usr/bin/env python3  
#-*- coding: utf-8 -*-

""" Cargar una lista de 10 enteros, luego mostrarlos por pantalla a cada elemento separados por una coma."""

def cargar():
    lista = []
    for x in range(10):
        valor = int(input("Ingrese el valor: "))
        lista.append(valor)
    return lista

def imprimir(lista):
    for x in range(len(lista)):
        print(lista[x], end="-")
    print("\n")
#Main block

lista = cargar()

imprimir(lista)
