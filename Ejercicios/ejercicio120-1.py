#!/usr/bin/env python
# -*- coding: utf-8 -*-


""" Confeccionar una función que le enviemos como parámetro el valor del lado de un cuadrado y nos retorne su superficie."""

def retornar_superficie(lado):

    sup = lado * lado

    return sup


#Bloque principal

va = int(input("Ingrese el valor de su lado"))

#Tenemos que almacenar lo que se devuelve en una variable que es global para que se muestre, si no esta no  muestra nada
#ya que tenemos una variable local de su funcion, y esta no puede ser sacada, es por eso que devolvemos el valor y despues lo guardamos en una variable
superficie = retornar_superficie(va)

print("La superficie es {}".format(retornar_superficie(va)))
