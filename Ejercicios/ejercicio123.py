#!/usr/bin/env python3
#-*- coding: utf-8 -*-


""" Elaborar una función que reciba tres enteros y 
nos retorne el valor promedio de los mismos."""





def promedio_funcion(valor1, valor2, valor3):
    
    suma = valor1 + valor2 + valor3

    promedio = suma / 3
    
    return promedio

v1 = int(input("Ingrese el primer valor: "))
v2 = int(input("Ingrese el segundo valor: "))
v3 = int(input("Ingrese el tercer valor: "))
print(promedio_funcion(v1, v2, v3))



