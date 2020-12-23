#!/usr/bin/env python3
#-*- coding: utf-8 -*-

""" Confeccionar un programa con las siguientes funciones:
1)Cargar una lista de 5 enteros.
2)Retornar el mayor y menor valor de la lista mediante una tupla.
Desempaquetar la tupla en el bloque principal y mostrar el mayor y menor. """

def cargar_valores():
    lista = []
    for x in range(5):
        valor = int(input("Ingrese el valor: "))
        lista.append(valor)
    return lista

def mayor_menor(lis):
    may = lis[0]
    men = lis[0]
    for x in range(len(lis)):
        if lis[x] > may:
            may = lis[x]
        if lis[x] < men:
            men = lis[x]
    return (may, men)


#MAIN BLOCK
leste = cargar_valores()
#Lo que se retorno se guardo en una tupla
tupla = mayor_menor(leste)
print(tupla)
mayor, menor = mayor_menor(leste)

print("El numero que es mayor a todos es {}".format(mayor))
print("El numero que es menor a todos es {}".format(menor))

