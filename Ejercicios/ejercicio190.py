#!/usr/bin/env python3
#-*- coding: utf-8 -*-

"""
Confeccionar una clase que represente un empleado. Definir como atributos su nombre y su sueldo. 
En el método __init__ cargar los atributos por teclado y luego en otro método imprimir sus datos y 
por último uno que imprima un mensaje si debe pagar impuestos (si el sueldo supera a 3000)
"""


class Empleado:
    def __init__(self):
        self.nombre = input("Ingrese el nombre del empleados: ")
        self.sueldo = int(input("Ingrese el sueldo de {}: ".format(self.nombre)))

    def imprimir(self):
        print("Nombre: {}".format(self.nombre))
        print("Sueldo: {}".format(self.sueldo))


    def paga_impuestos(self):
        if self.sueldo > 3000:
            print("{} debe de pagar impuestos".format(self.nombre))
        else:
            print("{} no debe de pagar impuestos".format(self.nombre))


#main block

empleado1 = Empleado()
empleado1.imprimir()
empleado1.paga_impuestos()
