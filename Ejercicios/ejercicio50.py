#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Confeccionar un programa que permita ingresar un valor del 1 al 10 y nos muestre la tabla de multiplicar del mismo (los primeros 12 términos)
Ejemplo: Si ingreso 3 deberá aparecer en pantalla los valores 3, 6, 9, hasta el 36."""


"""numero = int(input("Ingrese el numero del 1 al 10 que quiere multiplicar: \n"))
print("-------")
for f in range(1,11):
    multiplicacion = numero * f

    print(multiplicacion)
"""

numero = int(input("Ingrese el numero del 1 al 10 que quiere multiplicar: \n"))
if numero in range(10):
    regreso = True
else:
    regreso = False


while regreso == False:

    numero = int(input("Ingrese el numero del 1 al 10 que quiere multiplicar: \n"))

for f in range(1,11):
    multiplicacion = numero * f

    print(multiplicacion)
