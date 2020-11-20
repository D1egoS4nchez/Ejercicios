#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Escribir un programa que lea 10 números enteros y luego muestre cuántos valores ingresados fueron múltiplos de 3 y cuántos de 5.
Debemos tener en cuenta que hay números que son múltiplos de 3 y de 5 a la vez."""


multiplo3 = 0
multiplo5 = 0
for f in range(1,11):
    valor = int(input("Ingrese el valor del numero {}".format(f)))

    if valor % 3 == 0:
        multiplo3 += 1
    if valor % 5 == 0:
        multiplo5 += 1

print("Los numeros que se pueden dividir entre 3 son : {}".format(multiplo3))

print("Los numeros que se pueden dividir entre 5 son : {}".format(multiplo5))
