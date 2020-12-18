#!/usr/bin/env python3 
#-*- coding: utf-8 -*-

""" Definir una lista de enteros por asignación en el bloque principal. Llamar a una función que reciba la lista y 
nos retorne el producto de todos sus elementos. Mostrar dicho producto en el bloque principal de nuestro programa. """

def producto_elementos(owo):
    producto = 0
    posicion = 1
    for x in range(len(owo)):
        posicion =  posicion * owo[x]
    print(posicion)







#BLOQUE PRINCIPAL

lista = []
n = int(input("Ingrese cuantos valores quiere ingresar a la lista: "))

for x in range(n):
    valor = int(input("Ingrese su valor entero en la posicion numero {}: ".format(x)))
    lista.append(valor)

print(lista)

producto_elementos(lista)

