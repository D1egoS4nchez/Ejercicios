#!/usr/bin/env python3
# -*- coding: utf-8 -*-


""" Realizar un programa que pida la carga de dos listas numéricas enteras de 4 elementos cada una.
Generar una tercer lista que surja de la suma de los elementos de la misma posición de cada lista. Mostrar esta tercer lista. """

#Lista vacia para valores númericos
lista_numerica_1 = []
lista_numerica_2 = []


#En esta se va a guardar la suma de las listas anterriores
suma_dos_lista = []


print("Primera lista--------------------")
for x in range(4):

    valor = int(input("Ingrese el valor numero {}: ".format(x)))

    lista_numerica_1.append(valor)


print("Segunda lista--------------------")
for x in range(4):

    valor = int(input("Ingrese el valor numero {}: ".format(x)))

    lista_numerica_2.append(valor)

print("Suma de los valores en una lista--------------------")
for x in range(4):
    suma = lista_numerica_1[x] + lista_numerica_2[x]
    suma_dos_lista.append(suma)



#print(str(lista_numerica_1) + "\n" + str(lista_numerica_2))
