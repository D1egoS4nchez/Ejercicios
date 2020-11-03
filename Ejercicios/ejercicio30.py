#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def suma_while():
    x = 1
    suma = 0
    while x<=10:
        valor = int(input("Ingrese el numero que va a sumar: \n"))
        suma = suma + valor
        x = x + 1
    promedio = suma // 10
    print("La suma de los 10 valores que ingreso es: \n", suma)
    print("\t")
    print("El promedio es de: \t", promedio)

suma_while()
