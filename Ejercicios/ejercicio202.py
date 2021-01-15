#!/usr/bin/env python3
#-*- coding: utf-8 -*- 

"""
Declarar una clase Cuenta y dos subclases CajaAhorra y PlazoFijo. Definir los atributos y métodos comunes
entre una caja de ahorro y un plazo fijo y agruparlos en la clase Cuenta.
Una caja de ahorro y un plazo fijo tienen un nombre de titular y un monto. Un plazo fijo añade un plazo de imposición en días y una tasa de interés. 
Hacer que la caja de ahorro no genera intereses.
En el bloque principal del programa definir un objeto de la clase CajaAhorro y otro de la clase PlazoFijo.
"""

class Cuenta:

    def __init__(self):
        self.titular = input("Ingrese el nombre del propietario al que va a depositar: ")
        self.monto = int(input("Ingrese el monto que va a depositar en la cuenta de {}: "format(self.titular)))

    def imprimir(self):
        print("El titular de la caja es: {}".format(self.titular))
        print("Tiene un monto en su cuenta de {}".format(self.monto))

class CajaAhorro(Cuenta):
    

    def __init__(self):
        super.__init__()
        self.plazo = int(input("Ingrese de cuantos dias es el plazo: "))
        self.intereses = float(input("Ingrese el porcentaje de interes: "))

    def 


class PlazoFijo(Cuenta):


