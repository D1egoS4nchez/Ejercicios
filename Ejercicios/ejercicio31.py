#!/usr/bin/env python3
# -*- coding: utf-8 -*-
cantidad = 0
x = 1
n = int(input("Cuantas piezas cargara: \n"))
caliente = "caliente"
falso = "No se una medida que se pueda contar, ingrese la otra \t"
while x<=n:
    largo = float(input("Ingrese la medida \t \n"))
    if largo >= 1.2 and largo<=1.3:
        cantidad=cantidad+1
    else:
        print(falso)
    x=x+1
print("Las barras que estaban permitidas son {}, vuleva a ser {}".format(cantidad, caliente))
