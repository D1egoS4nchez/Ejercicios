#!/usr/bin/env python3  
#-*- coding: utf-8 -*-

#Importamos la libreria random
import random

"""
Confeccionar un programa que genere un número aleatorio entre 1 y 100 y no se muestre.
El operador debe tratar de adivinar el número ingresado.
Cada vez que ingrese un número mostrar un mensaje "Gano" si es igual al generado o "El número aleatorio es mayor" o "El número aleatorio es menor".
Mostrar cuando gana el jugador cuantos intentos necesitó.
"""

valor = random.randint(1,100)
pointer = False
s = "s"
while pointer == False and s == "s":
    n = int(input("Ingrese el valor: "))
    if n == valor:
        pointer = True
        print("Gano")
    else:
        print("El numero aleatorio es mayor")
        pass
    s = input("Quiere intentarlo otra vez?")
print(valor)
    
