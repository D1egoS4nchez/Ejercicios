#!/usr/bin/env python3  
#-*- coding: utf-8 -*- 

""" Almacenar los nombres de 5 productos y sus precios. Utilizar una lista y cada elemento una tupla con el nombre y el precio.
Desarrollar las funciones:
1) Cargar por teclado.
2) Listar los productos y precios.
3) Imprimir los productos con precios comprendidos entre 10 y 15. """


def cargar():
    #Referencia para hacer las pruebas
    n = int(input("Cuantos productos quiere ingresar"))
    #Hacemos una lista vacia para guardar las tuplas
    lista_productos = []
    #Bucle en el rango del numero que le ingresamos en la variable anteriormente
    for j in range(n):
        #Ingresamos en cada vuelta el valor que queramos, en este caso strings y numeros
        nombre = input("Ingrese el nombre del producto: ") 
        #Valores numericos referentes a la variable anterior
        valor = int(input("Ingrese el valor de {}: ".format(nombre)))
        #Juntamos en cada vuelta en una tupla los valores que se ingresaron
        lista_productos.append((nombre,valor))

    #Terminado el bucle devolvemos la lista de tuplas
    return lista_productos


def iterar_lis(lis):
    #Se ponen dos valores para las tuplas y que se vaya iterando en la lis

    #POnemos la j,k para desempaquetar las tuplas y se puedan acceder a ellas facilmente ;)
    for j,k in lis:
        #Imprimos los valores en cada vuelta que es una tupla en cada vuelta
        print(j, k)

def entre_10_15(z):
    conta = 0

    #Se pone dos letras que serian para las dos cosas que estan en la lista, o las dos tuplas para que se desempaquen

        #La "l" es para el primer objeto de la tupla que es nombre, y la "k" para el valor del producto
    for l,k in z:
        #Tomamos la k ya que es el producto y hacemos una condicion
        if k>10 and k<=15:
            print(l,k)
            #Si se cumple la funcion sumamos uno en cada vuelta
            conta += 1
    #Mandamos para imprimir cuantos objetos
    print("Hay {} productos que estan en el rangeo de 10-15 de valor".format(conta))

#MAIN BLOCK
lista = cargar()
iterar_lis(lista)
entre_10_15(lista)
