#!/usr/bin/env python3
#-*- coding: utf-8 -*-

"""
Implementar la clase Operaciones. Se deben cargar dos valores enteros por teclado en el método __init__, 
calcular su suma, resta, multiplicación y división, cada una en un método, imprimir dichos resultados.
"""

class Operaciones:

    def __init__(self):
        self.valor_1 = int(input("Ingrese el primer valor: "))
        self.valor_2 = int(input("Ingrese el segundo valor: "))


    def calcular(self):

        def suma():
            suma = self.valor_1 + self.valor_2
            print("La suma de {} y {} es {}".format(self.valor_1,self.valor_2, suma))
        

        def resta():
            if self.valor_1 > self.valor_2:
                resta =  self.valor_1 - self.valor_2
                print("La resta de {} y {} resulta {}".format(self.valor_1,self.valor_2,resta))
            else:
                resta = self.valor_2 - self.valor_1
                print("La resta de {} y {} resulta {}".format(self.valor_2,self.valor_1,resta))


        def multiplicar():
            multi = self.valor_1 * self.valor_2
            print("La multi de {} y {} resulta {}".format(self.valor_1,self.valor_2,multi))
    

        def division():
            if self.valor_1 > self.valor_2:
                div = self.valor_1 / self.valor_2
                print("La divsion de {} y {}, es {}".format(self.valor_1, self.valor_2, div))
            else:
                div = self.valor_2 / self.valor_1
                print("La divsion de {} y {}, es {}".format(self.valor_2, self.valor_1, div))

    

        suma()
        resta()
        multiplicar()
        division()

#MAIN BLOCK

operacion_1 = Operaciones()
operacion_1.calcular()
