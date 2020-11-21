#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Desarrollar un programa que solicite la carga de 10 números e imprima la suma de los últimos 5 valores ingresados. """

suma = 0
contador = 0
for f in range(1,11):
    numeros = int(input("Ingrese el numero {} de la lista: ".format(f)))
    if f >= 5:
        suma += numeros
print(suma)
