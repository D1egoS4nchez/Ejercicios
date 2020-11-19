#!/usr/bin/env python3
# -*- coding: utf-8 -*-


""" Realizar un programa que permita cargar dos listas de 15 valores cada una. Informar con un mensaje cual de las dos listas tiene un valor acumulado mayor (mensajes "Lista 1 mayor", "Lista 2 mayor", "Listas iguales")
Tener en cuenta que puede haber dos o más estructuras repetitivas en un algoritmo."""







sumatorio_lista_1 = 0

sumatorio_lista_2 = 0
i = 1

while i < 16:

    lista_1 = int(input("Ingrese el numero {} de la lista 1: \n".format(i)))

    lista_2 = int(input("Ingrese el numero {} de la lista 2: \n".format(i)))

    sumatorio_lista_1 = sumatorio_lista_1 + lista_1

    sumatorio_lista_2 = sumatorio_lista_2 + lista_2

    #print(sumatorio_lista_1, sumatorio_lista_2)
    i += 1


if sumatorio_lista_1 <= sumatorio_lista_2:
    print("Lista 1 es la mayor y su total es de {}".format(sumatorio_lista_1))
else:
    print("La lista 2 es mayor en valores, que su total es {}".format(sumatorio_lista_2))
