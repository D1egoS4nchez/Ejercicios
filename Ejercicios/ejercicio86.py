#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
En un curso de 4 alumnos se registraron las notas de sus exámenes y se deben procesar de acuerdo a lo siguiente:
a) Ingresar nombre y nota de cada alumno (almacenar los datos en dos listas paralelas)
b) Realizar un listado que muestre los nombres, notas y condición del alumno. En la condición, colocar "Muy Bueno" si la nota es mayor o igual a 8, "Bueno" si la nota está entre 4 y 7, y colocar "Insuficiente" si la nota es inferior a 4.
c) Imprimir cuantos alumnos tienen la leyenda “Muy Bueno”."""

nombre_lista = []
notas_lista = []

#Se hace un bucle para que se repita 4 veces, iniciando desde 1, esto se puede quitar, pero segun la comidad que le quieras tener, es mejor ponerlo
for x in range(1,4+1):
    nombre = input("Ingrese el nombre del alumno numero {}: ".format(x))

    nombre_lista.append(nombre)

#En este bucle se busca ingresar varios numeros en una lista, pero uno por uno y en cada vuelta sumandolos hasta que se complete el bucle, en este caso es 4
for x in range(4):
    nota_bucle = int(input("Ingrese la nota de {}: ".format(nombre_lista[x])))

    notas_lista.append(nota_bucle)


#Si imprimos la variable notas_lista, esta nos mostrará la lista, y los valores que se agregaron en cada vuelta.

""" Las siguientes listas vacias no son necesarias """
arriba_8 = []
rango_4_7 = []
abajo_de_4 = []

#Hacemos una lista vacia para guardar el valor que se clasifica de cada una si es que cumple alguna de las condiciones siguientes
condicion_alumno = []

# Inicializamos un contador para, vaya, contar lo que queramos agregar, en este caso si se cumple una funcion, sumar uno a su funcion
contador_muy_bueno = 0

#Hacemos un bucle for para checar varias condiciones, pero estas que en cada vuelta cheque pero la difernte posicion de la lista
for x in range(4):

    #Se busca que si el numero de la lista de la posicion x o el numero de la vuelta x sea mayor o igual a 8 para asi pasar a lo que debe de hacer
    if notas_lista[x] >= 8:
        #Se agrega en las listas vacias de su variable por si se llega a utilziae
        arriba_8.append(notas_lista[x])
                            #Por ahora no se necesitan

        #Se agrega el texto en la lista para, para asi cuando esta lista se use con otra, se pueda saber que se esta hablando de ese valor
        condicion_alumno.append("Muy bueno")

        #Si se cumole condicion pasada, la variable "contador_muy_bueno" sume 1 a el mismo
        contador_muy_bueno += 1
    else:#Se pone un else para que la siguiente funcion este anidada

        #En este if, se logra ver si el numero de la lista o el numero de vueta es mayor a 4
        if notas_lista[x] > 4: #Se puede poner ">= " pero esto nos dejaría limitados a más opciones, y la ultima opcion solo seria de 1-3
            rango_4_7.append(notas_lista[x])

            condicion_alumno.append("Bueno")
        else: #Aqui se usa else porque si esto no pasa, pasa lo contrario que es menos

            #En este se puede ver que el else, es "haz lo contrario" o haz lo siguiente, en este se ve que lo contrario de mayor es menor, asi que podemos poner las funciones correctas

                abajo_de_4.append(notas_lista[x])

                condicion_alumno.append("Insuficiente")

rango = 4

#Se hace un bucle for para iterar en las listas que hemos agregado y modificado.
for x in range(rango):

    #Aqui podemos ver que en estás listas, todas son del mismo tipo de longitud, y cada una de ellas son paralelas a las otraas
    #En cada iteracion, esta va a pasando por la misma posicion de cada una de la listas, y asi podemos sacar los valores para mostrarlos en la salida
    print("El alumno numero {}, se llama {} y este saco {}, se podria decir que esta en el rango de {}".format(x, nombre_lista[x], notas_lista[x],condicion_alumno[x]))
    print("---------------------------------------------------------------------------------------------------------------")

print("Hay {} alumnos que tienen una muy buena calificacion . ".format(contador_muy_bueno))
