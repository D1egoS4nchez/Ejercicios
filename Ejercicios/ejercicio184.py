#!/usr/bin/env python3  
#-*- coding: utf-8 -*-

# Definicion de un alias para una funcionalidad
    #El alias se pone con el as, entonces aqui si esta diciendo que la funcion se va a ejecutar con la palabra que le pongamos después de el "as"
                    
from math import sqrt as raiz, pow as elevar

valor = int(input("Ingrese un valor entero: "))
r1 = raiz(valor)
r2 = elevar(valor, 3)

print("La raiz cuadrada de {} es {}".format(valor, r1))
print("{} elevado al cubo es {}".format(valor, r2))
