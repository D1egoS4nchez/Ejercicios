#!/usr/bin/env python3  
#-*- coding: utf-8 -*-

""" 
Se desea almacenar los datos de 3 alumnos. Definir un diccionario cuya clave sea el número de documento del alumno. Como valor almacenar una lista con componentes de tipo tupla donde almacenamos nombre de materia y su nota.
Crear las siguientes funciones:
1) Carga de los alumnos (de cada alumno solicitar su dni y los nombres de las materias y sus notas)
2) Listado de todos los alumnos con sus notas
3) Consulta de un alumno por su dni, mostrar las materias que cursa y sus notas. 
"""


def charge():

    
    curricular = {}
    pointer1 = "s"
    while pointer1 == "s":
        num_doc = int(input("Ingrese el numero del documento del alumno: "))
        lista = []
        pointer2 = "s"
        while pointer2 == "s" or pointer2 == "S" or pointer2 == "si" or pointer2 == "SI":
            materia = input("Ingrese el nombre de la materia: "1)
            nota = int(input("Ingrese la nota que obtuvo en la materia: ")
            pointer2 = input("Quiere ingresar otra materia: [s/n]")
            lista.append((materia,nota))
        curricular[num_doc]=lista
    return curricular 

print(charge())
