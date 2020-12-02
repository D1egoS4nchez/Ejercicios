#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Crear una lista y almacenar los nombres de 5 países. Ordenar alfabéticamente la lista e imprimirla."""

lista_de_nombres = []

for x in range(5):
    valor = input("Ingrese el nombre del pais: \n")
    lista_de_nombres.append(valor)


for x in range(3):
    for k in range(4):

        if lista_de_nombres[x] > lista_de_nombres[x+1]:

            variable_aux = lista_de_nombres[x]

            lista_de_nombres[x] = lista_de_nombres[x+1]

            lista_de_nombres[x+1] = variable_aux


print(lista_de_nombres)
