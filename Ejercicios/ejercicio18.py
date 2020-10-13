# -*- coding: utf-8 -*-
dato1 = int(input("Ingrese la cantidad de preguntas del examen: \n"))

dato2 = int(input("Ingrese el numero de cantidad de respuestas correctas en el examen: \n"))

porcentaje = dato2 * 100 / dato1
def porcentajeDatos():
    print(porcentaje)

porcentajeDatos()

##def condicionPorcentaje():
if porcentaje >= 90:
    print("Esta en Nivel Máximo")
else:
    if porcentaje >= 75:
         print("Su calificacion esta en nivel medio")

    else:
        if porcentaje >= 50:
            print("Esta en un nivel regular")

        else:
            print("Esta fuera de nivel")
