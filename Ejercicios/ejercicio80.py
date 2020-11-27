#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Crear y cargar una lista con 5 enteros. Implementar un algoritmo que identifique el mayor valor de la lista


lista = []

for x in range(5):
    valor = int(input("Ingrese el valor: "))
    lista.append(valor)

mayor = 0

for x in range(5): # Lo que have es iterar en la lista
    if lista[x]>mayor:
        mayor = lista[x]
"""YA que estamos iterando, nos dice que si el numero x de la lista es mayor a la variable mayor,
entonces tenemos que remplzar esta variable y poner el numero de la vuelta es que es el mayor en ese mommento"""

print("Lista completa")
print(lista)
print(mayor)
