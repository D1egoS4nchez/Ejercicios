#!/usr/bin/env python3
#-*- coding: utf-8 -*-


""" Plantear una función que reciba un string en mayúsculas o minúsculas y retorne la cantidad de letras 'a' o 'A'. """


def recibir():
    sentece = input("Ingrese el string: \n")
    print("Esta es su frase: \n {}".format(sentece))
    return sentece
def checar():

    

    frase = recibir()
    retorno_numero = 0
    for x in range(len(frase)):
        if frase[x] == "a" or frase[x] == "A":
            retorno_numero += 1

    print("Su frase que ingreso tiene este numero de a (minusculass) y A(mayusculas) {} :" .format(retorno_numero))

#bloque principal

checar()


