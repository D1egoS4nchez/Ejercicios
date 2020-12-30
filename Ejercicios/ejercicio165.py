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
    while pointer1 == "s" or pointer1 == "si" or pointer1 == "S" or pointer1 == "SI":
        num_doc = int(input("Ingrese el numero del documento del alumno: "))
        lista = []
        pointer2 = "s"
        while pointer2 == "s" or pointer2 == "S" or pointer2 == "si" or pointer2 == "SI":
            materia = input("Ingrese el nombre de la materia: ")
            nota = int(input("Ingrese la nota que obtuvo en la materia: "))
            pointer2 = input("Quiere ingresar otra materia: [s/n]")
            lista.append((materia,nota))
        curricular[num_doc]=lista
        pointer1 = input("¿Quiere ingresar a otro alumno? [s/n]")
    return curricular

def listar(curricular):
    for numero in curricular: 
        print("El numero del alumno es: {}".format(numero))
        for j,k in curricular[numero]:
            print("El nombre de la materia es {} y obtuvo de calificacion un {}".format(j,k))

def consultar(curricular):
    pointer = "s"
    while pointer == "s" or pointer == "si" or pointer == "S" or pointer = "SI":
    
        dni_num = int(input("Ingrese el numero del estudiante que quiere buscar: "))
    
        if dni_num in curricular:
            for x,j in curricular[dni_num]:
                print(x,j, sep = "/")
        pointer = input("¿Quiere buscar a otro alumno? [s/n]")



def main()

#MAIN BLOCK
    curri = charge()
    listar(curri)
    consultar(curri)



