#!/usr/bin/env python3 
#-*- coding: utf-8 -*-

"""En Python se pueden definir parámetros y asignarles un dato en la misma cabecera de la función.
aLuego cuando llamamos a la función podemos o no enviarle un valor al parámetro.
Los parámetros por defecto nos permiten crear funciones más flexibles y que se pueden emplear en distintas circunstancias """
                            #Se hace una variable, y en esta se puede guardar, podemos modificar el valor de la variable a la horade llamar la funcion
                            #y poner el parametro en el cual esta la variable, y este parametro que le pongamos se va a guardar en la varible y si se necesita en la funcion
                            #se va a usar
def titulo_subrayado(titulo, caracter="*"):
    print(titulo)
    print(caracter*len(titulo))

#bloque main

titulo_subrayado("Sistema de Administracion")
titulo_subrayado("Ventas","-")
titulo_subrayado("Caca", ".")
