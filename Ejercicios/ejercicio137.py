#!/usr/bin/env python3
#-*- coding: utf-8 -*-

"""Confeccionar un programa que permita:
1) Cargar una lista de 10 elementos enteros.
2) Generar dos listas a partir de la primera. En una guardar los valores positivos y en otra los negativos.
3) Imprimir las dos listas generadas. """

def cargar():
    losta = []
    for x in range(10):
        valor = int(input("Ingrese el valor: "))
        losta.append(valor)
    return losta


def splito(lis):
    lis_pos = []
    lis_nega = []
    for x in range(10):
        lis_pos.append(lis[x])
        lis_nega.append(- + (lis[x]))
    return lis_pos, lis_nega
#Main block

def mainblock():
    lista = cargar()
    lista_positivia, lista_negativa = splito(lista)

    print("La lista positiva es esta: \n")
    for x in range(len(lista_positivia)):
        print("| "+ str(lista_positivia[x]) + " |")

    print("La lista negativa es: ")
    for w in range(len(lista_negativa)):
        print("| " + str(lista_negativa[w]) + " |")

mainblock()
