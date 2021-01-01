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
    while continua == "s" or continua == "S" or continua == "si":
        valor = int(input("Ingrese un valor: "))
        lista.append(valor)
        continua = input("Agrega otra elemento a la lista: [s/n]")
    return lista





def fijar_cero(li):
    for x in range(len(li)):
        if li[x]<10:
            li[x]=0 

def imprimir(lista):
    for elemento in lista:
        print(elemento,"-",sep="",end="")
    print("")











#MAINBLOCK

def main():

    lista = cargar()
    imprimir(lista)
    fijar_cero(lista)
    imprimir(lista)

main()
