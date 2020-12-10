#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Desarrollar un programa que permita ingresar el lado de un cuadrado. Luego preguntar si quiere calcular y mostrar su perímetro o su superficie. """


def mostrar_permitro(lado):
    per = lado * 4
    print("El perimetro es {}".format(per))


def mostrar_superficie(lado):
    sup = lado * lado
    print("La superficie es {}".format(sup))

def cargar_dato():
    la = int(input("Ingrese el valor del lado de un cuadrado"))

    respuesta = input("Quiere calcular el perimetro o la superficie [ingrese texto: perimetro/superficie]?")
    if respuesta == "perimetro":
        mostrar_perimetro(la)
    if respuesta == "superficie":
        mostrar_superficie(la)


#programa principial

cargar_dato()
