#!/usr/bin/env python3
# -*- coding: utf-8 -*-

sueldos = []


for x in range(5):
    valor = int(input("Ingrese el sueldo: \n"))
    sueldos.append(valor)

for k in range(4):
    for x in range(4):
        if sueldos[x]>= sueldos[x+1]:
            aux = sueldos[x]

            sueldos[x] = sueldos[x+1]

            sueldos[x+1] = aux

print("Lista con elos elementos ordenados:")
print(sueldos)
