#!/usr/bin/env python3  
#-*- coding: utf-8 -+-

""" Almacenar en una lista de 5 elementos las tuplas con el nombre de empleado y su sueldo.
Implementar las funciones:
1) Carga de empleados.
2) Impresión de los empleados y sus sueldos.
3) Nombre del empleado con sueldo mayor.
4) Cantidad de empleados con sueldo menor a 1000. """

def cargar():
    empleados = 0
    for x in range(5):
        nombre = input("Ingrese el nombre: ")
        sueldo = int(input("Ingrese el sueldo: "))
        empleados.append((nombre,sueldo))
    return empleados


def imprimir(empleados):
    print("Listado de los nombres de empleados y sus sueldos")
    for nombre,sueldo in empleados:
        print(nombre,sueldo)



def mayor_sueldo(empleados):
    empleado = empleados[0]
    for emp in empleados:
        if emp[1]>empleado[1]:
            empleado = emp
    print("Empleado con mayor sueldo es:",empleado[0]
