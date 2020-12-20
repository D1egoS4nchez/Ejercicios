#!/usr/bin/env python3
#-*- coding: utf-8 -*-

""" Desarrollar una aplicación que permita ingresar por teclado los nombres de 5 artículos y sus precios.
Definir las siguientes funciones:
1) Cargar los nombres de articulos y sus precios.
2) Imprimir los nombres y precios.
3) Imprimir el nombre de artículo con un precio mayor
4) Ingresar por teclado un importe y luego mostrar todos los artículos con un precio menor igual al valor ingresado. """



def cargar():
    lista_articulos = []
    lista_precios = []
    for x in range(5):
        articulo = input("Ingrese el nombre del articulo: ")
        lista_articulos.append(articulo)
        precio = int(input("Ingrese el valor del articulo {}: ".format(lista_articulos[x])))
        lista_precios.append(precio)
    #Se retorna las lista dentro de una lista
    return [lista_articulos, lista_precios] 


def impresion(lista_1, lista_2):
    for k in range(5): 
        print(lista_1[k]+ " " + str(lista_2[k]))


def checadita(lista_1, lista_2):
    piv = lista_2[0]
    contador = 0
    for x in range(5):
        for w in range(x-1):
            if lista_2[w]>piv:
                piv = {lista_2[w], lis_1[w]}
                
    return piv

    #return contador 



#MAIN BLOCK 
lis_1, lis_2 = cargar()
impresion(lis_1, lis_2)
pivoteo = checadita(lis_1, lis_2)

print("El mayor es {}".format(pivoteo))
