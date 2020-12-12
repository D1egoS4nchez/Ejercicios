#!/usr/bin/env python3
#-*- coding: utf-8 -*-

def largo(cadena):
 
    #Devolvemos el valor , que seria lo largo de la cadena, este devolera
    return len(cadena)

#Bloque principal

nombre1 = input("Ingrese primer nombre: ")
nombre2 = input("Ingrese su segundo nombre: ")
#Se guarda el valor que es la longitud de la cadena pero con el parametro que se le metio que es la variable
la1 = largo(nombre1)
la2 = largo(nombre2)

if la1 == la2:
    print("Iguales los nombres {} y {}".format(nombre1, nombre2))
elif la1 > la2:
    print("Es mayor el primer nomvbre qu es {}". format(nombre1))
else:
    print("Es mayor el segundo nombre que es {}".format(nombre2))


