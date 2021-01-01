#!/usr/bin/env python3  
#-*- coding: utf-8 -*-


"""
Confeccionar un programa que almacene en un diccionario como clave el nombre de un contacto y como valor su número telefónico:
1) Carga de contactos y su número telefónico.
2) Pemitir modificar el número telefónico. Se ingresa el nombre del contacto para su búsqueda.
3) Imprimir la lista completa de contactos con sus números telefónicos.
"""

def cargar():
    contactos = {}
    continua = "s"
    while continua == "s" or continua == "S" or continua == "SI":
        nombre = input("Ingres el nombre del contacto: ")
        telefono = int(input("Ingrese el numero de contacto: "))
        contactos[nombre]=telefono
        continua = input("¿Quiere ingresar otro contacto? [s/n]")
    return contactos

def modificar_telefono(con):
    nombre = input("Ingrese el nombre que quiere modificar el numero telefonico")
    if nombre in con:
        telefono = int(input("Ingrese el nuevo contacto: "))
        con[nombre]=telefono
    else:
        print("No hay ningun numero telefonico con ese nombre.")

def imprimir(contactos):
    for k in contactos:
        print(k, contactos[k],sep="Numero:")



def main():
    contactos = cargar()
    modificar_telefono(contactos)
    imprimir(contactos)

main()
