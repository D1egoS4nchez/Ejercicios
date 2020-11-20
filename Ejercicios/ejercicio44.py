#!/usr/bin/env python3
# -*- coding: utf-8 -*-


""" Escribir un programa que solicite por teclado 10 notas de alumnos y nos informe cuántos tienen notas mayores o iguales a 7 y cuántos menores. """

contador_7 = 0
contador_mas_7 = 0
for f in range(1,11):
    nota_alumno = int(input("Ingrese la nota del {} alumno".format(f)))

    if nota_alumno <= 7:
        contador_7 += 1
    else:
        contador_mas_7 += 1

print("El numero de alumnos que tiene 7 o menos de 7: {} ".format(contador_7))
print("El numero de alumnos que tiene arriba de 7 son: {}".format(contador_mas_7))
