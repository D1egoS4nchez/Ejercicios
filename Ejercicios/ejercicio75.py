#!/usr/bin/env python3
# -*- coding: utf-8 -*-


#Definimos una lista vacia

lista = []

#disponemos de un cliclo de 5 vueltas

for x in range(1,5+1):
    valor = int(input("Ingrese el valor {} entero: ".format(x)))

    lista.append(valor)

print(lista)
