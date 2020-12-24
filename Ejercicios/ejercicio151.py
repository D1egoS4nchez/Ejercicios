#!/usr/bin/env python3
#-*- coding: utf-8 -*-

empleado = ["juan",53, (25,11,1999)]
print(empleado)
#Se trata de agregar o modificar una tupla, en este caso la que esta adentro de la lista, entonces como una tupla no se puede modificar, esta
#no se agrega y mantiene el valor que le fue puesto, en cambio, si se quiere modifcar lo que esta en la lista, se puede hacerlo
empleado.append((1,1,2016))
alumno = ("pedro",[7,9])
print(alumno)
#En este si se puede hacer aunque este dentro de una tupla porque estamos modificando una lista, en este le estamos agregando un valor a la lista
alumno[1].append(10)
print(alumno)
