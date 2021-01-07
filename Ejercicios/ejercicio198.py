#!/usr/bin/env python3
#-*- coding: utf-8 -*-

"""
Plantear un programa que permita jugar a los dados. Las reglas de juego son:
se tiran tres dados si los tres salen con el mismo valor mostrar un mensaje que "gano", sino "perdió".
"""
import random 

class Dado:
    def tirar(self):
        #Hacemos un atributo llamado valor que tiene adentro un numero aleatorio de un rango de 1 a 6
        self.valor = random.randint(1,6)

    def imprimir(self):
