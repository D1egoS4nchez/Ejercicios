#!/usr/bin/env python3
#-*- coding: utf-8 -*-

"""
Plantear un programa que permita jugar a los dados. Las reglas de juego son:
se tiran tres dados si los tres salen con el mismo valor mostrar un mensaje que "gano", sino "perdió".
"""
import random 


#Clase para cada dado
class Dado:
    def tirar(self):
        #Hacemos un atributo llamado valor que tiene adentro un numero aleatorio de un rango de 1 a 6
        self.valor = random.randint(1,6)

    def imprimir(self):
        print("Valor del dado {}".format(self.valor))

    def retonar_valor(self):

        return self.valor

#Clase para utilizar los objetos y usar los metodos dentro de la clase anterior y estos meterlos adentro de un metodo
class JuegoDeDados:


    def __init__(self):
        #Hacemos un objeto con la clase Dado
        #Objeto uno llamado dado1
        self.dado1 = Dado()
        #Objeto llamado dado2
        self.dado2 = Dado()
        #Objeto llamado dado3
        self.dado3 = Dado()
    
    def jugar(self):
        self.dado1.tirar()
        self.dado1.imprimir()
        self.dado2.tirar()
        self.dado2.imprimir()
        self.dado3.tirar()
        self.dado3.imprimir()
        if self.dado1.retonar_valor() == self.dado2.retonar_valor() and self.dado1.retonar_valor()==self.dado3.retonar_valor():
            print("Gano")
        else:
            print("Perdio")



juego_dados = JuegoDeDados()
juego_dados.jugar()
