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
        #
        fecha = input("Ingrese la fecha con formaton dd/mm/aa: ")
        continua2 = "s"
        lista = []
        while continua2 == "s":
            hora = input("Ingrese la hora con formato hh:mm ")
            actividad = input("Ingrese la descripcion de la actividad: ")
            lista.append((hora.actividad))
            continua2 = input("Ingrese otra actividad para la misma fecha[s/n]: ")
        agenda[fecha]=lista
        continua1 = input("Ingresa otra fecha [s/n]: ")
    return agenda

def imprimir(agenda):
    print("Listado completa de la agenda")
    for fecha in agenda:
        print("Para la fecha: {}".format(fecha))
        for hora,actividad in agenda[fecha]:
            print(hora,actividad)



def consulta_fecha(agenda):
    fecha = int(input("Ingrese la fecha que desea consultar: "))
    if fecha in agenda:
        for hora,actividad in agenda[fecha]:
            print(hora,actividad)
        else:
            print("No hay actividades agendadas para dicha fecha")


    
#MAIN
agenda = cargar()
imprimir(agenda)
consulta_fecha(agenda)