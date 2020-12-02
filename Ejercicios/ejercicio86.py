#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
En un curso de 4 alumnos se registraron las notas de sus exámenes y se deben procesar de acuerdo a lo siguiente:
a) Ingresar nombre y nota de cada alumno (almacenar los datos en dos listas paralelas)
b) Realizar un listado que muestre los nombres, notas y condición del alumno. En la condición, colocar "Muy Bueno" si la nota es mayor o igual a 8, "Bueno" si la nota está entre 4 y 7, y colocar "Insuficiente" si la nota es inferior a 4.
c) Imprimir cuantos alumnos tienen la leyenda “Muy Bueno”."""

nombre_lista = []
notas_lista = []


for x in range(1,4+1):
    nombre = input("Ingrese el nombre del alumno numero {}: ".format(x))

    nombre_lista.append(nombre)

for x in range(4):
    nota_bucle = int(input("Ingrese la nota de {}: ".format(nombre_lista[x])))

    notas_lista.append(nota_bucle)

arriba_8 = []
rango_4_7 = []
abajo_de_4 = []

condicion_alumno = []
contador_muy_bueno = 0
for x in range(4):
    if notas_lista[x] > 7:
        arriba_8.append(notas_lista[x])

        condicion_alumno.append("Muy bueno")

        contador_muy_bueno += 1

    if notas_lista[x] < 6 or     notas_lista[x] > 4:

        rango_4_7.append(notas_lista[x])

        condicion_alumno.append("Bueno")

    else:

        if notas_lista[x] < 4:


            abajo_de_4.append(notas_lista[x])

            condicion_alumno.append("Insuficiente")

print(condicion_alumno)
print("Hay {} alumnos que tienen Muy bueno. ".format(contador_muy_bueno))
