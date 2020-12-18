#!/usr/bin/env python3
#-*- coding: utf-8 -*-

""" Desarrollar una función que reciba una lista de string y nos retorne el que tiene más caracteres. Si hay más de uno con dicha cantidad de caracteres debe retornar el que tiene un valor de componente más baja.
En el bloque principal iniciamos por asignación la lista de string:
palabras=["enero", "febrero", "marzo", "abril", "mayo", "junio"]
print("Palabra con mas caracteres:",mascaracteres(palabras)) """

def checadita(lista_string):
    #Se hace una variable para guardar el valor 0
    pos = 0
    for x in range(len(lista_string)):
        #En esta condicion se checa el largo de la palabra de la lista de la vuelta x, y para hacer la condicion pone la posicion la variable pos
        if len(lista_string[x]) > len(lista_string[pos]):

            #Si se cumple la posicion, la variable se remplaza con el numero de vuelta y vuelve a pasar, con esto vemos que a la hora si ya no se cumple la condicion
            #esta se queda con el numero de vuelta y sabemos que palabra es ya que podemos verlo indexando con la lista y la variable que es un numero
            pos = x
    return lista_string[pos]



    


#bloque principal

#Se hace una lista con las palabras
palabras=["enero", "febrero", "marzo", "abril", "mayo", "junio"]
print("Palabra con mas caracteres:",checadita(palabras))
