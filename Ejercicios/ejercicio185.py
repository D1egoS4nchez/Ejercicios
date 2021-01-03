#!/usr/bin/env python3
#-*- coding: utf-8 -*-

"""
Calcular el factorial de un número ingresado por teclado.
El factorial de un número es la cantidad que resulta de la multiplicación de determinado número natural por todos los números naturales que le anteceden excluyendo el cero. Por ejemplo el factorial de 4 es 24, que resulta de multiplicar 4*3*2*1.
No hay que implementar el algoritmo para calcular el factorial sino hay que importar dicha funcionalidad del módulo math.
El módulo math tiene una función llamada factorial que recibe como parámetro un entero del que necesitamos que nos retorne el factorial.
Solo importar la funcionalidad factorial del módulo math de la biblioteca estándar de Python.
"""

#Del modulo math importamos la funcion factorial y le ponemos como alias a esta la palabra k_l
from math import factorial as k_l

#Ingresamos el valor que va a hacer la funcion factorial
valor = int(input("Ingrese el valor: "))
#Guardamos en una variable el resultado de la funcion con el valor para asi despues mostrarla
resultado = k_l(valor)
#Imprimos el valor de la funcion
print("El factorial es {}".format(resultado))
