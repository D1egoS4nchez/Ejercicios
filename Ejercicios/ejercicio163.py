#!/usr/bin/env python3  
#-*- coding: utf-8 -*-

""" Confeccionar un programa que permita cargar un código de producto como clave en un diccionario. Guardar para dicha clave el nombre del producto, su precio y cantidad en stock.
Implementar las siguientes actividades:
1) Carga de datos en el diccionario.
2) Listado completo de productos.
3) Consulta de un producto por su clave, mostrar el nombre, precio y stock.
4) Listado de todos los productos que tengan un stock con valor cero. """

def cargar():
    productos = {}
    continua = "s"
    while continua == "s" or continua == "S" or continua == "si":
        codigo = int(input("Ingrese el codigo del producto: "))
        descripcion  = input("Ingrese la descripcion: ")
        precio = float(input("Ingrese el precio del producto: "))
        stock = int(input("Ingrese el stock actual: " ))
        #                     [0]       [1]     [2]
        productos[codigo]=(descripcion,precio, stock)
        continua = input(" ¿Desea caragr otro producto [s/n]?")
    return productos

def imprimir(productos):
    print("Listado completo de productos")
    for key in productos:
        #En este caso usamos el indexado de la tupla
        #Para indexar tenemos que ponernos en la parte del diccionario del valor que es diccionario[key][valor que queremos mostrar ya que es una tupla]
        print(key,productos[key][0],productos[key][1],productos[key][2])


def consulta(productos):
    codigo = int(input("Ingrese el codigo de articulo al consultar: "))
    if codigo in productos:
        print(productos[codigo][0],productos[codigo][1],productos[codigo][2])

def listado_stock_cero(productos):
    print("Listado de articulos con stock en cero:")
    #Hacemos un bucle para iterar en el diccionario con la clave en el diccionario que en este caso es llamado codigo
    for codigo in productos:
        #Checamos en los valores en la posicion dos si este tiene un valor 0, si es asi este imprimira toda la informacion 
        if productos[codigo][2]==0:
            print(codigo,productos[codigo][0],productos[codigo][1],productos[codigo][2])



# bloque principal

productos=cargar()
imprimir(productos)
consulta(productos)
listado_stock_cero(productos)

