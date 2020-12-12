#!/usr/bin/env python3  
#-*- coding: utf-8 -*-

""" Confeccionar una función que calcule la superficie de un rectángulo y la retorne, la función recibe como parámetros los valores de dos de sus lados:
def retornar_superficie(lado1,lado2): """


def calcular_sup_rectangulo(altura, ancho):

    superficie = altura * ancho

    return superficie

al = int(input("Ingrese la altura de rectángulo: "))
an = int(input("Ingrese el ancho de su rectangulo: "))

print("La superficie del triangulo es {}". format(calcular_sup_rectangulo(al, an)))
    
