#!/usr/bin/env python3
#-*- coding: utf-8 -*-

def retornar_mayor(v1,v2):
    if v1>v2:
        mayor = v1
    else:
        mayor = v2
    return mayor
#Bloque principal

numero_1 = int(input("Ingrese su primer valor: "))
numero_2 = int(input("Ingrese su segundo valor: "))

print("El numero mayor de los dos numeros anteriores que ingreso es: ")
print(retornar_mayor(numero_1, numero_2))
