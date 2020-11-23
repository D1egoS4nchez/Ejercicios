#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Ingresar una oración que pueden tener letras tanto en mayúsculas como minúsculas.
Contar la cantidad de vocales. Crear un segundo string con toda la oración en minúsculas para que sea más fácil disponer la condición que verifica que es una vocal."""

oracion_normal = input("Ingrese su oracion: \n")
x = 0

contador_vocales = 0
while x < len(oracion_normal):
    if oracion_normal[x] == "a" or oracion_normal[x] == "e" or oracion_normal[x] == "i" or oracion_normal[x] == "o" or oracion_normal[x] == "u":
        contador_vocales += 1

    x += 1

print("El numero de vocales que tiene su frase es de {} vocales".format(contador_vocales))
def volver_mayus():
    decision = input("Quiere volver su oracion en mayúsculas? [y/n]: ")
    if decision == "y":
        decision_bool = True
    if decision == "n":
        decision_bool = False

    if decision_bool == True:
        print("Vamos volver a su frase a mayúsculas")
        oracion_mayusculas = oracion_normal.upper()

        print(oracion_mayusculas)
    else:
        print("Pues no se va a poder convertir en mayuscula su frase {}".format(oracion_normal))

volver_mayus()
