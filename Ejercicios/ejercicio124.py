#!/usr/bin/env python3
#-*- coding: utf-8 -+-

""" Elaborar una función que nos retorne el perímetro 
de un cuadrado pasando como parámetros el valor de un lado."""


def retornar_perimetro_cuadrado(lado):
    perimetro = lado * 4
    return perimetro

figura = int(input("Cuantos lados tiene su figura"))
la = int(input("Ingrese el valor del lado"))


if figura == 4:
    print(retornar_perimetro_cuadrado(la))

