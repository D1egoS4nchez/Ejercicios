#!/usr/bin/env python3
#-*- coding: utf-8 -*-


""" 
Confeccionar una agenda. Utilizar un diccionario cuya clave sea la fecha. Permitir almacenar distintas actividades para la misma fecha (se ingresa la hora y la actividad)
Implementar las siguientes funciones:
1) Carga de datos en la agenda.
2) Listado completo de la agenda.
3) Consulta de una fecha.
"""

#Funcion para cargar valores en el diccionario
def cargar():
    
    #Creamos un diccionario vacio
    agenda = {}
    #Hacemos un puntero para el while
    continua1 = "s"
    #Hacemos un while para ingresar datos en el diccionario
    while continua1 == "s":
        #Guardamos un valor en la variable
        fecha = input("Ingrese la fecha con formaton dd/mm/aa: ")
        #Hacemos un puntero para hacer otro while, en este caso es un bucle dentro de uno para ingresar otro tipo de informacion
        continua2 = "s"
        #Hacemos una lista vacia
        lista = []
        #Hacemos otro while para guardar los valores en la lista y no se tenga problemas x
        #Hacemos un while para continuar en el bucle

        #Este while permitira ingresar los valores del diccionario o de la clave pero en una lista 
        while continua2=="s":
            hora=input("Ingrese la hora de la actividad con formato hh:mm ")
            actividad=input("Ingrese la descripcon de la actividad:")
            #Agregamos los valores anteriormente ingresados en una lista
            lista.append((hora,actividad))
            #Hacemos un while para agregar mas actividades, y con este podemos agregar más
            continua2=input("Ingresa otra actividad para la misma fecha[s/n]:")
        #Agregamos los valores en el diccionario, la lista como el valor de la clave que es la variable fecha
        agenda[fecha]=lista
        #Con este puntero podemos repetir el bloque principal que es agregar una fecha
        continua1=input("Ingresa otra fecha[s/n]:")
     #Retornamos el diccionario para guardarlo en una variable o imprimirlo
    return agenda

#Funcion para imprimir el diccionario que retornamos en la funcion pasada, en esta ponemos como parametro el valor agenda que es el diccionario
def imprimir(agenda):
    #Imprime un mensaje
    print("Listado completa de la agenda")
    #Iteramos en el diccionario con la clave que es la fecha
    for fecha in agenda:
        #Imprime lo que es la clave del diccionario
        print("Para la fecha: {}".format(fecha))
        #Hacemos otro for para iterar en la lista o el valor que contiene anidada una lista para asi desempaquetarlos o entrar en el valor del diccionario
        for hora,actividad in agenda[fecha]:
            #En este ya se tiene desempaquetado lo que es la lista o el valor en el diccionario, depues de la parte agenda ponemos lo que es la clave que seria en dicci[valor], esto para no meternos en la parte incorrecta 
            #y que imprima correctamente lo que son los valores de la lista que esta adentro de la seccion valor del diccionario 
            print(hora,actividad)

#Podemos hacer un while para repetir esta funcion con un puntero

def consulta_fecha(agenda):
    #Ingresamos un valor para buscar en el diccionario
    fecha = int(input("Ingrese la fecha que desea consultar: "))
    #Si esta el valor que ingresamos en la variable, esta imprimira lo que son los valores
    if fecha in agenda:
        #Asi que iteramos en el valor del diccionario que es poniendo los dos valores 
        for hora,actividad in agenda[fecha]:
            #Imprimimos los valores de las posiciones
            print(hora,actividad)
    #Si no se cumple la condicion anterior esta mostrará un mensaje de que no esta disponible o no fue ingresada en el diccionario 
    else:
        print("No hay actividades agendadas para dicha fecha")


    
def main():

    agenda = cargar()
    imprimir(agenda)
    point = "s"
    while point == "s" or point == "S" or point == "si" or point == "SI":
        consulta_fecha(agenda)
        point = input("¿Quiere buscar otra fecha? [s/n]")

main()
