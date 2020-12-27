#!/usr/bin/env python3  
#-*- coding: utf-8 -*-

""" Confeccionar un programa que permita la carga de una lista de 5 enteros por teclado.
Luego en otras funciones:
1) Imprimirla en forma completa.
2) Obtener y mostrar el mayor.
3) Mostrar la suma de todas sus componentes.
Utilizar la nueva sintaxis de for vista en este concepto. """

#Funcion para cargar la lista
def cargar():
    #Se hace una lista vacia
    lista = []
    #Bucle para agregar un valor en la variable num cada vuelta
    for x in range(5):
        num = int(input("Ingrese un valor: "))
        #En cada vuelta se agrega el valor anterior en la lista vacia
        lista.append(num)
    #Se retorna la lista con los numeros ya ingresafd
    return lista

#Funcion para imprimir cada elemento de la lista, con el parametro que en este caso es la lista que se devolvio anteriormente en la funcion cargar                              
def imprimir(lista):

    print("Lista completa")
    #La palabra elemento es igual a poner un x, en este caso lo no es necesario poner la lista y el elemento
    for elemento in lista:
        #Itera en cada elemento en la lista
        #Imprime el elemento en cada vuelta
        print(elemento, end="-")
    print("\n")

#Funcion para sacar el mayor ;)

def mayor(lista):
    #Guardamos la primera posicion de la lista en una variable para comparar
    may = lista[0]
    #Iteramos en la lista 
    for elemento in lista:
        #La condicion dice que si el elemento de la lista o el elemento que toque ve si se cumple la condicion
        if elemento>may:
            #Si cumple la condicion lo que hará es sobreescribir el valor de la posicion o el valor de la vuelta que cumple la condicion
            may = elemento
    print("El elemento mayor de la lista es: {}".format(may))


"""def prueba(lista):
    for uno in lista:
        print(uno,"\ ")"""


#Funcion para sumar todos los elementos iterando en cada elemento de la lista, asi guardando en la variable el resultado 
def suma_elementos(lista):
    suma = 0

    for elemento in lista:
        suma = suma + elemento
    print("La suma de todos sus elementos es {}".format(suma))

#MAIN BLOCK

#BLOQUE PRINCIPAL PARA EJECUTAR TODAS LAS FUNCIONES
def  mainblock():
    lista = cargar()
    prueba(lista)
    imprimir(lista)
    mayor(lista)
    suma_elementos(lista)


mainblock()
