#!/usr/bin/env python3
# -*- coding: utf-8 -*-


""" Desarrollar un programa que permita cargar 5 nombres de personas y sus edades respectivas.
Luego de realizar la carga por teclado de todos los datos imprimir los nombres de las personas mayores de edad (mayores o iguales a 18 años) """

nombres = []

edad_lista = []

rango_pete = 5

for x in range(5):

    nombre_valor = input("Ingrese el nombre del sujeto {}: ".format(x))
    nombres.append(nombre_valor)

for x in range(5):

    edad_valor = int(input("Ingrese su la edad del sujeto {}".format(nombres[x])))

    edad_lista.append(edad_valor)

def checar_edad():
    for x in range(rango_pete):
        if edad_lista[x]>18 and edad_lista[x]<=20:
            count = 0
            count += 1

    print("Hay {} personas que estan en el rango de 18 a 20".format(count))

checar_edad()
