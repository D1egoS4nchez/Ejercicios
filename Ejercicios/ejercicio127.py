#!/usr/bin/env python3
#-*- coding: utf-8 -*-

#Funciones parametros lista


#Se hace una funcion para sumar toda la lista
def sumarizar(lista):
    #Se inicializa una variable para guardar el resultado en cada vuelta
    suma=0

    #Se hace un for para iterar en la lista
    for x in range(len(lista)):

        #En cada vuelta se suma la posicion 
        suma=suma+lista[x]

    #Se devuelve lo que es la variable
    return suma


def mayor(lista):
    may=lista[0]
    for x in range(1,len(lista)):
        if lista[x]>may:
            may=lista[x]
    return may


def menor(lista):
    men=lista[0]

    #Se hace un bucle for pero la primera posicion en la queinicia es uno y se toma lo largo el largo 
    for x in range(1,len(lista)):

        #Hacemos una condicion que si se cumple se guarda el numero en la variable 
        if lista[x]<men:
            men=lista[x]
    return men
    

# bloque principal del programa

listavalores=[10, 56, 23, 120, 94]
print("La lista completa es")
print(listavalores)
print("La suma de todos su elementos es", sumarizar(listavalores))
print("El mayor valor de la lista es", mayor(listavalores))
print("El menor valor de la lista es", menor(listavalores))
