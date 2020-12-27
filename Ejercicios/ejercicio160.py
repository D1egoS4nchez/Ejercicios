#!/usr/bin/env python3  
#-*- coding: utf-8 -*-

""" Crear un diccionario que permita almacenar 5 artículos, utilizar como clave el nombre de productos y como valor el precio del mismo.
Desarrollar además las funciones de:
1) Imprimir en forma completa el diccionario
2) Imprimir solo los artículos con precio superior a 100. 
"""

def cargar():
    productos = {}
    for x in range(5):
        nombre = input("Ingrese el nombre del producto")
        precio = int(input("Ingrese el precio de {}: ".format(nombre)))
        #Nombre de la lista, despues la clave y por ultimo el valor que se le va a poner a la clave
        productos[nombre]=precio
    return productos

def imprimir(pro):
    print("La lista de productos es: \n {}".format(pro))
    for j in productos:
        print(j, productos[j])

def imprimir_mayor100(productos):
    print("Listado de articulos con precios mayores a 100")
    for nombre in productos:
        if productos[nombre]>100:
            print(nombre)    


# bloque principal

productos=cargar()
imprimir(productos)
imprimir_mayor100(productos)

