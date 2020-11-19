#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Desarrollar un programa que permita cargar n números enteros y luego nos informe cuántos valores fueron pares y cuántos impares.
Emplear el operador “%” en la condición de la estructura condicional (este operador retorna el resto de la división de dos valores, por ejemplo 11%2 retorna un 1): """


x = 1

n_numeros = int(input("Ingrese el las veces que quiere ingresar el numero y checar si es par o impar: \n"))

while x <= n_numeros:
    numerito = int(input("Ingrese el numero {}: \n".format(x)))
    contador_par = 0
    contador_impar = 0

    if numerito % 2 == 0:

        contador_par += 1
    else:
        if numerito % 1 == 0 and numerito % numerito == 0:
            contador_impar += 1



    x += 1

print(contador_par,contador_impar)
