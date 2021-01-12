#!/usr/bin/env python3
#-*- coding: utf-8 -*-

"""
Plantear una clase Persona que contenga dos atributos: nombre y edad. Definir como responsabilidades la carga por teclado y su impresión.
En el bloque principal del programa definir un objeto de la clase persona y llamar a sus métodos.

Declarar una segunda clase llamada Empleado que herede de la clase Persona y agregue un atributo sueldo y muestre si debe pagar impuestos (sueldo superior a 3000)
También en el bloque principal del programa crear un objeto de la clase Empleado.
"""

class Persona:
    

    def __init__(self):

        self.nombre = input("Ingrese el nombre: ")
        self.edad = int(input("Ingrese la edad: "))


    def imprimir(self):
        print("Nombre: ",self.nombre)
        print("Edad: ",self.edad)


class Empleado:

    def __init__(self):
        super().__init__()
        self.sueldo = float(input("Ingrese el sueldo de {}: ".format(self.nombre)))


    def imprimir(self):
        super().imprimir()
        print("Sueldo: ".format(self.sueldo))


    def paga_impuestos(self):
        if self.sueldo > 3000:
            print("Debe de pagar impuestos {}".format(self.nombre))
        else:
            print("No debe de pagar impuestos {}".format(self.nombre))


#MAIN BLOCK

persona1 = Persona()
persona1.imprimir()
print("_____________________________")

empleado1 = Empleado()
empleado1.imprimir()
empleado1.paga_impuestos()
