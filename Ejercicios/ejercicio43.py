#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Desarrollar un programa que permita la carga de 10 valores por teclado y nos muestre posteriormente la suma de los valores ingresados y su promedio.
Este problema ya lo desarrollamos, lo resolveremos empleando la estructura for para repetir la carga de los diez valores por teclado."""

suma = 0
for f in range(1,11):
    valor = int(input("Ingrese el {} valror: \n".format(f)))

    suma = suma + valor

print("La suma es")

print(suma)

promedio = suma/10

print("El promedio es {}".format(promedio))
