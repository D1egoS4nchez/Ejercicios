#!/usr/bin/env python3  
#-*- coding: utf-8 -*- 
""" 
Se desea almacenar los datos de 3 alumnos. Definir un diccionario cuya clave sea el número de documento del alumno. Como valor almacenar una lista con componentes de tipo tupla donde almacenamos nombre de materia y su nota.
Crear las siguientes funciones:
1) Carga de los alumnos (de cada alumno solicitar su dni y los nombres de las materias y sus notas)
2) Listado de todos los alumnos con sus notas
3) Consulta de un alumno por su dni, mostrar las materias que cursa y sus notas. 
"""

a#FUNCION PARA CARGAR LOS VALORES EN EL DICCIONARIO, en este caso sera lo que es el numero del estudiante como clave y como valor, el nombre de la materia y la nota que saco en ella
def charge():

    #Diccionario vacio  #Diccionario vacio   
    curricular = {}
    #   Pointer para hacerl el while
    pointer1 = "s"
    while pointer1 == "s" or pointer1 == "si" or pointer1 == "S" or pointer1 == "SI":
        #Ingresamos el valor para la clave del diccionario
        num_doc = int(input("Ingrese el numero del documento del alumno: "))
        #Hacemos una lista vacia para agregar los valores como tuplas en una 
        lista = []
        #Hacemos otro puntero para agregar dos valores pero esto para agregar mas valores de este tipo en el diccionario como tuplas
        pointer2 = "s"
        #Hacemos un while con condiciones 
        while pointer2 == "s" or pointer2 == "S" or pointer2 == "si" or pointer2 == "SI":
            #Ingresamos el nombre de la materia
            materia = input("Ingrese el nombre de la materia: ")
            #Ingresamos la nota que saco el alumno de la materia que ingresamos 
            nota = int(input("Ingrese la nota que obtuvo en la materia: "))
            #Sobreescribimos en la variable    
            pointer2 = input("Quiere ingresar otra materia: [s/n]")
            #Agregamos los valores en una tupla en una lista: variables --> tuplas --> diccionario
            lista.append((materia,nota))
        #Agregamos la lista con tuplas en el valor del diccionario
        curricular[num_doc]=lista
        #Sobreescribimos la variable del primer while
        pointer1 = input("¿Quiere ingresar a otro alumno? [s/n]")
    #Retornamos el diccionario 
    return curricular


#Funcion para listar el diccionario pero con una buena presentación
def listar(curricular):
    #Hacemos un for para la clave del diccionario
    for numero in curricular: 
        print("El numero del alumno es: {}".format(numero))
        #Hacemos otro bucle para desempaquetar la lista en el valor
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


main()
