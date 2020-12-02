#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Cargar una lista con 5 elementos enteros. Ordenarla de menor a mayor y mostrarla por pantalla, luego ordenar de mayor a menor e imprimir nuevamente."""

lista_principal = []

menor_mayor = []

for p in range(5):
    valor_entero = int(input("Ingrese el valor: "))

    lista_principal.append(valor_entero)

menor_mayor = lista_principal
mayor_menor = lista_principal
for k in range(4):
    for x in range(4):
        if menor_mayor[x] > menor_mayor[x+1]:

            aux_1 = menor_mayor[x]

            menor_mayor[x] = menor_mayor[x+1]

            menor_mayor[x+1] = aux_1

print(menor_mayor)

for k in range(4):
    for x in range(4):
        if mayor_menor[x] < mayor_menor[x+1]:

            aux_1 = mayor_menor[x]

            mayor_menor[x] = mayor_menor[x+1]

            mayor_menor[x+1] = aux_1
