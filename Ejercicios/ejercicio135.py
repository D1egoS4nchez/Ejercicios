#!/usr/bin/env python3
#-*- coding: utf-8 -*-


"""
En una empresa se almacenaron los sueldos de 10 personas.
Desarrollar las siguientes funciones y llamarlas desde el bloque principal:
1) Carga de los sueldos en una lista.
2) Impresión de todos los sueldos.
3) Cuántos tienen un sueldo superior a $4000.
4) Retornar el promedio de los sueldos.
5) Mostrar todos los sueldos que están por debajo del promedio. """

def cargar_lista():
    lista = []
    for x in range(10):
        valorsto = int(input("Ingrese el valo que quiere cara de pija: "))
        lista.append(valorsto)
    return lista

def impresion():
    print(cargar_lista())

#MAIN BLOCK
impresion()
