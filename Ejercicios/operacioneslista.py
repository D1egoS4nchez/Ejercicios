#!/usr/bin/env python3
#-*- coding: utf-8 -*-


def cargar():
    lista = []
    for x in range(5):
        valor = int(input("Ingrese su valor: "))
        lista.append(valor)
    return lista


def imprimir_mayor(lista):
    may = lista[0]
    for x in range(1,5):
        if lista[x] > may:
            may = lista[x]

    print("El mayor de la lista es {}".format(may))


def imprimir_suma(lista):
    suma = 0
    for x in lista:
        suma += x

    print("La suma de los valores son {}".format(suma))


