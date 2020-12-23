#/usr/bin/env python3   
#-*- coding: utf-8 -*-


def cargar_empleado():
    nombre=input("Ingrese el nombre del empleado:")
    sueldo=float(input("Ingrese su sueldo:"))
    return (nombre,sueldo)

def compar(emp1, emp2):

        if emp1[1] > emp2[1]:
            return emp1[0]
        else:
            return emp2[0]

#MAIN BLOCK

empleado1 = cargar_empleado()
empleado2 = cargar_empleado()

mayor = compar(empleado1, empleado2)
print("El empleado que gana mas se llama {}".format(mayor))
