#!/usr/bin/env python3
# -*- coding: utf-8 -*-


""" Confeccionar un programa que lea n pares de datos, cada par de datos corresponde a la medida de la base y la altura de un triángulo. El programa deberá informar:
a) De cada triángulo la medida de su base, su altura y su superficie.
b) La cantidad de triángulos cuya superficie es mayor a 12. """


n_datos = int(input("Ingrese cuantos pares de datos quiere ingresar: \n"))
n_datos += 1
contador_puto = 0
for m in range(1,n_datos):
    base = float(input("Ingrese la base del {} par: \n".format(m)))
    print("-----------")
    altura = float(input("Ingrese la altura del {} par: \n".format(m)))
    print("-----------")
    superficie = base * altura

    if superficie >= 12:
        contador_puto += 1

print("\n")

print("Los rectangulos que tienen una area mayor a doce son {} \n".format(contador_puto))

"""quiere_triangulo = input("Quiere calcular con los datos que ingreso el area de un triangulo?: \n [y=yes / n=no]")


if quiere_triangulo == "y":
    print("Arre pa")
"""
