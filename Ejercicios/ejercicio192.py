#!/usr/bin/env python3
#-*- coding: utf-8 -*-

#Importamos la funcion pow
from math import pow

"""
Desarrollar una clase que represente un Cuadrado y tenga los siguientes métodos: inicializar el valor del lado 
llegando como parámetro al método __init__ (definir un atributo llamado lado), imprimir su perímetro y su superficie.
"""
#Se hace una clase llamada Cuadrado con dos metodos
class Cuadrado:
    #Incializamos el valor y lo hacemos un atributo
    def __init__(self,lado):
        self.lado = lado

    #Hacemos un metodo para imprimir la superficie y el perimetor 
    def imprimir(self):
        #Para sacar el valor utilizamos la funcio pow
        print("Su superficie es {}".format(pow(self.lado,2)))
        print("Su perimetro es {}".format(self.lado * 4))



#MAIN BLOCK
#Hacemos un objeto llamado cuadrado que contiene los metodos que esta adentro de la clase Cuadrado
        #Llamamos a la clase e ingresamos como parametro el valor del lado
cuadrado = Cuadrado(6)
#Tomamos el objeto y ponemos uno de los metodo de la clase que es imprimir, este hará lo que esta adentro del de metodo imprimir
cuadrado.imprimir()
