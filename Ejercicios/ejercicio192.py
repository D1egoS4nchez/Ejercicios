#!/usr/bin/env python3
#-*- coding: utf-8 -*-
import math

"""
Desarrollar una clase que represente un Cuadrado y tenga los siguientes métodos: inicializar el valor del lado 
llegando como parámetro al método __init__ (definir un atributo llamado lado), imprimir su perímetro y su superficie.
"""

class Cuadrado:

    def __init__(self,lado):
        self.lado = lado


    def imprimir(self):
        print("Su superficie es {}".format(pow(self.lado,2)))
        print("Su perimetro es {}".format(self.lado * 4))



#MAIN BLOCK

cuadrado = Cuadrado(6)
cuadrado.imprimir()
