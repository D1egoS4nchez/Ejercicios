#!/usr/bin/env python3
#-*- coding: utf-8 -*-

"""Confeccionar un programa que permita:
1) Cargar una lista de 10 elementos enteros.
2) Generar dos listas a partir de la primera. En una guardar los valores positivos y en otra los negativos.
3) Imprimir las dos listas generadas. """

def cargar():
    #Se hace una lista vacia para guarda los valores
    losta = []
    #Hacemos un bucle para iterar
    for x in range(10):
        #Hacemos una variable que guarde en cada vuelta el valor que se le meta
        valor = int(input("Ingrese el valor: "))
        #En cada vuelta se agrega el valor que se guardo en la variable
        losta.append(valor)
    #Se regresa el la lista para mostrarla después
    return losta


def splito(lis):
    #Se hace dos listas para guardar los datos positivos y negativos
    lis_pos = []
    lis_nega = []
    #Un bucle para iterar en la lista y agregar en cada lista segun lo que pongamos
    for x in range(10):
        #Se agrega el valor normal
        lis_pos.append(lis[x])
        #Se agrega el valor x de la lista y antes se pone un signo negativo 
        lis_nega.append(- + (lis[x]))
    return lis_pos, lis_nega
#Main block
#Se hace una funcion para tenerlo mas ordenado
def mainblock():
    lista = cargar()
    lista_positivia, lista_negativa = splito(lista)

    print("La lista positiva es esta: \n")
    for x in range(len(lista_positivia)):
        print("| "+ str(lista_positivia[x]) + "  |")

    print("La lista negativa es: ")
    for w in range(len(lista_negativa)):
        print("| " + str(lista_negativa[w]) + "  |")

mainblock()
