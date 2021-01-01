#!/usr/bin/env python3  
#-*- coding: utf-8 -*-

"""
Crear un diccionario en Python para almacenar los datos de empleados de una empresa. La clave será su número de legajo y en su valor almacenar una lista con el nombre, profesión y sueldo.
Desarrollar las siguientes funciones:
1) Carga de datos de empleados.
2) Permitir modificar el sueldo de un empleado. Ingresamos su número de legajo para buscarlo.
3) Mostrar todos los datos de empleados que tienen una profesión de "analista de sistemas"
"""

#FUNCIO PARA CARGAR DATOS
def cargar():
    #Hacemos un diccionario vacio
    datos = {}
    #Se hace una variable para luego modificarla y usarla después como un puntero
    continua = "s"
    #Este while dice que mientras la variable contengan un s va a repetir el bloque tiene dentro
    while continua == "s":
        #Ingresamos el numero del empleado en la variable
        numero = int(input("Ingrese el numero de legajo del empleado: "))
        #Hacemos una lista vacia para meter tuplas en ella
        lista = []
        #Ingresamos el nombre del empleado que queremos ingresar
        nombre = input("Ingrese el nombre del empleado: ")
        #Agregamos el nombre de la profesion
        profesion = input("¿Cuál es la profesión del empleado?: ")
        #Agregamos el sueldo en la variable sueldo
        sueldo = float(input("Ingrese el sueldo que tiene el empleado: "))
        #Agregamos las variables en una tupla y esta tupla en la lista
        lista.append((nombre,profesion,sueldo))
        #Agregamos el numero como clave y la lista como el valor
        datos[numero]=lista
        #Modificamos el puntero para seguir ejecutando nuevamente el bloque anterior
        continua = input("¿Quiere ingresar a otro empleado? [s/n]")
    #Se devuelve el diccionario que anteriormente agregamos datos
    return datos

#
def imprimir(datos):
    print("Listado completo de empleados")
    for k in datos:
        print(k,datos[k][0],datos[k][1],datos[k][2])

def modificar(dat):
    num = int(input("Ingrese el numero de empleado que quiere que se modifique el sueldo: "))
    if num in dat:
        nuevoSaldo = float(input("Ingrese la nueva cantidad que quiere modifcar"))
        dat[num][2]=nuevoSaldo
    else:
        print("No existe ningun empleado con ese numero")


def analistas(datos):
    for j in datos:
        if datos[j][1] == "analista de sistemas":
            print(j,datos[j][0],datos[j][2])

datos = cargar()
imprimir(datos)
modificar(datos)
analistas(datos)
