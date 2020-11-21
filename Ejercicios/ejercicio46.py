#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Codificar un programa que lea n números enteros y calcule la cantidad de valores mayores o iguales a 1000 (n se carga por teclado)
Este tipo de problemas también se puede resolver empleando la estructura repetitiva for.
Lo primero que se hace es cargar una variable que indique la cantidad de valores a ingresar. Dicha variable se carga antes de entrar a la estructura repetitiva for. """

cantidad = 0
n  = int(input("Ingrese cuantos valores quiere ingresar en el programa: \n"))

inicio = 1
for f in range(n):
    valor = int(input("Ingrese el valor del numero {}: \n".format(f)))

    if valor >= 1000:
        cantidad += 1

print("La cantidad de valores asignados mayores o iguales son: {}".format(cantidad))
