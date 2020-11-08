#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" En una empresa trabajan n empleados cuyos sueldos oscilan entre $100 y $500, realizar un programa que
lea los sueldos que cobra cada empleado e informe cuántos empleados cobran entre $100 y $300 y cuántos cobran más de $300.
Además el programa deberá informar el importe que gasta la empresa en sueldos al personal. """

n = int(input("Ingrese cuanto empleados quiere ingresar su sueldo: \n "))
x = 1
contador1 = 0
contador2 = 0
while x <= n:
    sueldo = int(input("Ingrese el sueldo del {} \n".format(x))
    if sueldo >= 100 and sueldo2 <= 300:
        contador1 = contador1 + 1
    else:
        if sueldo >= 301 and sueldo2 <= 500:
            contador2 = contador2 + 1
    x = x + 1

print(contador1)

print(contador2)
