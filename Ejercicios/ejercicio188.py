#!/usr/bin/env python3  
#-*- coding: utf-8 -*-

""" 
Confeccionar una clase que permita carga el nombre y la edad de una persona.
Mostrar los datos cargados. Imprimir un mensaje si es mayor de edad (edad>=18)
"""

class Persona:

    def inicializar(self):
        nombre = input("Ingrese el nombre:")
        self.nombre = nombre
        edad = int(input("Ingrese la edad de {}:".format(self.nombre)))
        self.edad = edad

    def imprimir(self):
        print("{} tiene {} años".format(self.nombre, self.edad))
    
    def mayor_edad(self):
        if self.edad >= 18:
            print("{} es mayor de edad".format(self.nombre))
        else:
            print("{} no es mayor de edad".format(self.nombre))


def main():

    persona1 = Persona()
    persona1.inicializar()
    persona1.imprimir()
    persona1.mayor_edad()


    persona2 = Persona()
    persona2.inicializar()
    persona2.imprimir()
    persona2.mayor_edad()
main()
