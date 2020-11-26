#!/usr/bin/env python3
# -*- coding: utf-8 -*-

lista = []

valor = int(input("Ingrese el valor(0 para finalizar): "))

while valor != 0:
    lista.append(valor)
    valor = int(input("Ingrese el valor(0 para finalizar): "))


print("Tamaño de la lista: {} ".format(len(lista)))
print(lista)
