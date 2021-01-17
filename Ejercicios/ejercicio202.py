#!/usr/bin/env python3  
#-*- coding: utf-8 -*- 

""" 
Declarar una clase Cuenta y dos subclases CajaAhorra y PlazoFijo. Definir los atributos y métodos comunes entre una caja de ahorro y un plazo fijo y agruparlos en la clase Cuenta.
Una caja de ahorro y un plazo fijo tienen un nombre de titular y un monto. Un plazo fijo añade un plazo de imposición en días y una tasa de interés. Hacer que la caja de ahorro no genera intereses.
En el bloque principal del programa definir un objeto de la clase CajaAhorro y otro de la clase PlazoFijo.
"""



class Cuenta:
    

    def __init__(self):
        self.nombre = input("Ingrese el nombre del dueño de la cuenta: ")   
        self.monto = int(input("Ingres el monto: "))

    def imprimir(self):
        print(self.nombre, self.monto, sep = " ")

class CajaAhorra(Cuenta):
    

    def __init__(self):
        super.__init__()

    def imprimir(self):
        print("Cuenta de caja de ahorro")
        super.imprimir()

class PlazoFijo(Cuenta):



