#!/usr/bin/env python3
#-*- coding: utf-8 -*-

"""Desarrollar una aplicación que nos permita crear un diccionario ingles/castellano. La clave es la palabra en ingles y el valor es la palabra en castellano.
Crear las siguientes funciones:
1) Cargar el diccionario.
2) Listado completo del diccionario.
3) Ingresar por teclado una palabra en ingles y si existe en el diccionario mostrar su traducción. """


def cargar():
    diccionario = {}
    continua = "s"
    while continua == "s":
        caste = input("Ingrese la palabra en castellano: ")
        ing = input("Ingrese la palabra en ingles: ")
        diccionario[ing]=caste
        continua = input("¿Quiere agregar mas palabras?[s/n] \n")
    return diccionario


def imprimir(dic):
    print("Listado completo del diccionario\n")
    for j in dic:
        print(j,dic[j])


def search_words(dic):
    pal = input("Ingrese la palabra en ingles que quiere buscar: ")
    if pal in dic:
        print("En castellano significa {}".format(dic[pal]))


# bloque principal

diccionario=cargar()
imprimir(diccionario)
search_words(diccionario)
