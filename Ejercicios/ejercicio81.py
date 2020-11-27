#!/usr/bin/env python3
# -*- coding: utf-8 -*-


lista = []

for x in range(5):
    valor = int(input("Ingrese el numero {} de la lista: ".format(x)))
    lista.append(valor)

menor = lista[0]
posicion = 0

"""#Se hace un bucle for, y nos dice que vamos a repetir la accion que esta dentro del bloque de codigo,
la condicion que esta dice, que va a checar en cada vuelta la lista[x]  si es menor,y si se cumple la funcion
if este aplicará la orden que se puso, esto se va a repetir en cada vuelta, pero si el numero de la lista de la vueltas
no es menor, este no se hará nada y repetirá la vuelta.
"""
for x in range(1,5):

    if lista[x]<menor:

        menor = lista[x]
        posicion = x
print("Lista completa")
print(lista)
print("Menor de la lista")
print(menor)
print("Posicion del menor en la lista")
print(posicion)
