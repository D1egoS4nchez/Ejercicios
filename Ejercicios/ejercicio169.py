#!/usr/bin/env python3  
#-*- coding: utf-8 -*-

"""
Crear un diccionario en Python para almacenar los datos de empleados de una empresa. La clave será su número de legajo y en su valor almacenar una lista con el nombre, profesión y sueldo.
Desarrollar las siguientes funciones:
1) Carga de datos de empleados.
2) Permitir modificar el sueldo de un empleado. Ingresamos su número de legajo para buscarlo.
3) Mostrar todos los datos de empleados que tienen una profesión de "analista de sistemas"
"""

def cargar():
    datos = {}
    continua = "s"
    while continua == "s":
        numero = int(input("Ingrese el numero de legajo del empleado: "))
        lista = []
        nombre = input("Ingrese el nombre del empleado: ")
        profesion = input("¿Cuál es la profesión del empleado?: ")
        sueldo = int(input("Ingrese el sueldo que tiene el empleado: "))
        lista.append((nombre,profesion,sueldo))
        datos[numero]=lista
        continua = input("¿Quiere ingresar a otro empleado? [s/n]")
    return continua

print(cargar())
