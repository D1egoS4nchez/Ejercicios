#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Solicitar por teclado la cantidad de empleados que tiene la empresa. Crear y cargar una lista con todos los sueldos de dichos empleados.
Imprimir la lista de sueldos ordenamos de menor a mayor."""

lista_sueldos = []
n = int(input("Cuantos sueldos quiere ingresar: \n"))

for x in range(n):
    sueldo = int(input("Ingresee el sueldo numero {}: ".format(x)))
    lista_sueldos.append(sueldo)

print("Está es la lista de los sueldos sin ordenar \n {}".format(lista_sueldos))


for k in range(n-1):
    for p in range(n-1):
        if lista_sueldos[p] > lista_sueldos[p+1]:

            aux = lista_sueldos[p]

            lista_sueldos[p] = lista_sueldos[p+1]

            lista_sueldos[p+1] = aux



print(lista_sueldos)
