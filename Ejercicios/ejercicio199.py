#!/usr/bin/env python3
#-*- coding: utf-8 -*-
"""
Plantear una clase Club y otra clase Socio.
La clase Socio debe tener los siguientes atributos: nombre y la antigüedad en el club (en años).
En el método __init__ de la clase Socio pedir la carga por teclado del nombre y su antigüedad.
La clase Club debe tener como atributos 3 objetos de la clase Socio.
Definir una responsabilidad para imprimir el nombre del socio con mayor antigüedad en el club.
"""

class Socio:
    

    def __init__(self):
        self.nombre = input("Ingrese su nombre: ")
        self.antiguedad = int(input("Ingrese la antiguedad que tiene el socio {} en el club: ".format(self.nombre)))

    def imprimir(self):
        print(self.nombre, "tiene {} años de antiguedad".format(self.antiguedad))

    def retornar_anos(self):
        return self.antiguedad

    def retornar_nom(self):
        return self.nombre
class Club:
    

    def __init__(self):
        self.socio_1 = Socio()
        self.socio_2 = Socio()
        self.socio_3 = Socio()
        self.imprimir()

    def imprimir(self):
        self.socio_1.imprimir()
        self.socio_2.imprimir()
        self.socio_3.imprimir()

    def mayor(self):
        if (self.socio_1.retornar_anos() > self.socio_2.retornar_anos() and self.socio_1.retornar_anos() > self.socio_3.retornar_anos()):
            print(self.socio_1.retornar_nom())
        else:
            if (self.socio_2.retornar_anos() > self.socio_3.retornar_anos()):
                print(self.socio_2.retornar_nom())
            else:
                print(self.socio_3.retornar_nom())


#MAIN BLOCK

bethis = Club()
bethis.mayor()
