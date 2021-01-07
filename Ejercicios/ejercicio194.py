#!/usr/bin/env python3
#-*- coding: utf-8 -*-

"""
Plantear una clase Operaciones que solicite en el método __init__ la carga de dos enteros e inmediatamente 
muestre su suma, resta, multiplicación y división. Hacer cada operación en otro método de la clase Operación
y llamarlos desde el mismo método __init__

"""


class Operacion:

    def __init__(self):
        self.valor1 = int(input("Ingrese el primer valor: "))
        self.valor2 = int(input("Ingrese el segundo valor: "))
        self.sumar()
        self.restar()
        self.multiplicar()
        self. dividir()
    

    def sumar(self):

        sumar = self.valor2 + self.valor1
        print("La sumas es: {}".format(self.sumar))

    
    def restar(self):

        if self.valor1 > self.valor2:
            
            restar = self.valor1 - self.valor2
            print("El resultado de restar {} y {} da {}".format(self.valor1, self.valor2, restar))


        else:

            restar = self.valor2 - self.valor1
            print("El resultado de restar {} y {} da {}".format(self.valor2, self.valor1, restar))

    def multiplicar(self):

        multiplicar = self.valor1 * self.valor2
        print("El producto de {} y {} es: {}".format(self.valor1, self.valor2, multiplicar))


    def dividir(self):

        if self.valor1 > self.valor2:
            dividir =  self.valor1/self.valor2
            print("La division da {}".format(dividir))
        else:
            dividir = self.valor2/self.valor2
            print("La division da {}".format(dividir))


Sopa = Operacion()

