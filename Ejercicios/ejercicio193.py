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
            self.suma = self.valor_1 + self.valor_2
            print("La suma de {} y {} es {}".format(self.valor_1,self.valor_2, suma))
        

        def resta():
            if self.valor_1 > self.valor_2:
                self.resta =  self.valor_1 - self.valor_2
                print("La resta de {} y {} resulta {}".format(self.valor_1,self.valor_2,self.resta))
            else:
                self.resta = self.valor_2 - self.valor_1
                print("La resta de {} y {} resulta {}".format(self.valor_2,self.valor_1,self.resta))


        def multiplicar():
            self.multi = self.valor_1 * self.valor_2
            print("La multi de {} y {} resulta {}".format(self.valor_1,self.valor_2,self.multi))
    

        def division():
            if self.valor_1 > self.valor_2:
                self.div = self.valor_1 / self.valor_2
                print("La divsion de {} y {}, es {}".format(self.valor_1, self.valor_2, self.div))
            else:
                self.div = self.valor_2 / self.valor_1
                print("La divsion de {} y {}, es {}".format(self.valor_2, self.valor_1, self.div))

    

        suma()
        resta()
        multiplicar()
        division()
    

    def imprimir(self):
        print(self.suma)
        print(self.resta)
#MAIN BLOCK

operacion_1 = Operaciones()
operacion_1.calcular()
operacion_1.imprimir()

