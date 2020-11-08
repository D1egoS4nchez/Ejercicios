#!/usr/bin/env python3
# -*- coding: utf-8 -*-

x = 1


suma_alturas = 0
n = int(input("Ingrese cuantas personas quiere ingresar: \n"))
while x<=n:
    alturas_personas = int(input("Ingrese la altura en cms: \n"))
    suma_alturas = suma_alturas + alturas_personas
    x = x + 1
promedio_altura = suma_alturas / n
print("El promedio de alturas de las personas ingresadas es de: \t", promedio_altura)
