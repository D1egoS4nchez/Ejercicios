#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Crear y cargar en un lista los nombres de 5 países y en otra lista paralela la cantidad de habitantes del mismo.
Ordenar alfabéticamente e imprimir los resultados. Por último ordenar con respecto a la cantidad de habitantes (de mayor a menor) e imprimir nuevamente."""

paises = []

habitantes = []

for x in range(5):
    pa = input("Ingrese el nombre de país: ")

    paises.append(pa)

    ha = int(input("Ingrese cuantos habitantes tiene ese país: "))

    habitantes.append(ha)


if
    for k in range(4):
        for x in range(4-k):
            if paises[x] > paises[x+1]:
                aux_paises = paises[x]
                paises[x] = paises[x+1]
                paises[x+1] = aux_paises


                aux_habitantes = habitantes[x]
                habitantes[x] = habitantes[x+1]
                habitantes[x+1] = aux_habitantes

else:
    for k in range(4):
        for x in range(4-k):
            if habitantes[x] > habitantes[x+1]:

                aux_habitantes = habitantes[x]
                habitantes[x] = habitantes[x+1]
                habitantes[x+1] = aux_habitantes
                aux_paises = paises[x]
                paises[x] = paises[x+1]
                paises[x+1] = aux_paises
