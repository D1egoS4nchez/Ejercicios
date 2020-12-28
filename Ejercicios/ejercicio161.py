#!/usr/bin/env python3
#-*- coding: utf-8 -*-

"""Desarrollar una aplicación que nos permita crear un diccionario ingles/castellano. La clave es la palabra en ingles y el valor es la palabra en castellano.
Crear las siguientes funciones:
1) Cargar el diccionario.
2) Listado completo del diccionario.
3) Ingresar por teclado una palabra en ingles y si existe en el diccionario mostrar su traducción. """

#Funcion para cargar valores en el diccionario
def cargar():
    #Hacemos un diccionario vacio
    diccionario = {}
    #Un puntero para hacer un while
    continua = "s"
    #Si se cumple la condicion se va a hacer el bloque de codigo 
    #Este nos dice que mientras la variable sea igual a "s" ejecute este bloque de código 
    while continua == "s":
        #Se ingresa una entrada en la variable
        caste = input("Ingrese la palabra en castellano: ")
        #Se ingresa la palabra en ingles
        ing = input("Ingrese la palabra en ingles: ")
        #Se agrega los valores ingresados anteriormente
        diccionario[ing]=caste
        #Hacemos un input para modificar el valor y ver si se cumple la condicion otra vez
        continua = input("¿Quiere agregar mas palabras?[s/n] \n")
    #Devolvemos el diccionario con los valores anteriormente ingresados
    return diccionario

#Funcion para imprimir el diccionario 
def imprimir(dic):
    print("Listado completo del diccionario\n")
    #Se toma la clave para iterar en el diccionario
    for j in dic:
        #Se imprime la clave y el valor de la clave, el ultimo  para imprimirlo debe de ponerse asi: diccionario[clave]
        print(j,dic[j])


def search_words(dic):
    #Ingresamos la palabra que queremos buscar 
    pal = input("Ingrese la palabra en ingles que quiere buscar: ")
    #Hacemos una condicion para ver si esta la clave en el diccionario con la variable y la palabra in con el diccionario
    if pal in dic:

        print("En castellano significa {}".format(dic[pal]))


# bloque principal
#FUNCIONES
diccionario=cargar()
imprimir(diccionario)
search_words(diccionario)
