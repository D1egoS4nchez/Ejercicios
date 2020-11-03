#!/usr/bin/env python3
# -*- coding: utf-8 -*-
x = 1
n = 10
notas_menores = 0

while x<=10:
    notas_alumnos = int(input("Ingrese la nota del alumno {}: \n".format(x)))
    if notas_alumnos < 7:
        notas_menores = notas_menores + 1
    x = x+1
print(notas_menores)
