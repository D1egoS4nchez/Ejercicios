#!/usr/bin/env python3  
#-*- coding: utf-8 -*-

""" Crear un diccionario en Python que defina como clave el número de documento de una persona y como valor un string con su nombre.
Desarrollar las siguientes funciones:
1) Cargar por teclado los datos de 4 personas.
2) Listado completo del diccionario.
3) Consulta del nombre de una persona ingresando su número de documento. """


def cargar():
    diccionario = {}
    whil = "s"
    while whil == "s" or  whil == "S"  or whil == "si":
        num_doc = int(input("Ingrese el numero de documento de la persona: "))
        nombre = input("Ingrese el nombre de una persona")
        diccionario[num_doc]=nombre
        whil = input("Quiere ingresar otro numero y nombre?: [s/n]")

    return diccionario

def listado(dic):
    print("Numero / Nombre")
    for x in dic:
        print(x, dic[x], sep="/",)
        
def checada(dic):
    



    #MAIN BLOCK

dic = cargar()
listado(dic)
checada(dic)
