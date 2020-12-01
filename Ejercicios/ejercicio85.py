#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Crear y cargar dos listas con los nombres de 5 productos en una y sus respectivos precios en otra. Definir dos listas paralelas. Mostrar cuantos productos tienen un precio mayor al primer producto ingresado. """



def hacer_listas():
    # Se inicializan las listas en variables
    lista_nombre = []
    precio_productos = []

    #Se repite varias veces la entrada para que se guarden en la lista
    for x in range(1,5+1):
        nombre_producto = input("Ingrese el nombre del {} producto: \n".format(x))

        #Se agrega el producto que se ingreso cada vuelta
        lista_nombre.append(nombre_producto)

    #Se hace un bucle para ignresar los precios
    for x in range(5):

        #Se hace una variable para que guarde la variable
        producto_precio = int(input("Ingrese el precio del producto {}: \n".format(lista_nombre[x])))

        #Se agrega el valor de la variable producto_precio en la lista, cada vez 
        precio_productos.append(producto_precio)


    producto_mayor_precio = precio_productos[0]

    contador = 0

    for x in range(5):
        if precio_productos[x] < producto_mayor_precio:
            contador += 1

    print("Hay {} productos que son mayores al primero".format(contador))

hacer_listas()
