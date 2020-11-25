#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Definir una lista por asignación que almacene en la primer componente el nombre de un alumno y en las dos siguientes sus notas.
Imprimir luego el nombre y el promedio de las dos notas."""


lista=["ana", 7, 9]
print("El nombre del alumno es {}".format(lista[0]))

promedio = lista[1] + lista[2] // 2

print("El promedio del alumno es de {}".format(promedio))
