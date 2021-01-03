#!/usr/bin/env python3
#-*- coding: utf-8 -*-

from math import sqrt,pow

valor = int(input("Ingrese el valor: "))
r1 = sqrt(valor)
r2 = pow(valor,2)
print("La raiz cuadrada de {} es {}".format(valor, r1))
print("El cubo de {} es {}".format(valor, r2))
