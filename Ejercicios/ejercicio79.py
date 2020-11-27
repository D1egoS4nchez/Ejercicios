#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Una empresa tiene dos turnos (mañana y tarde) en los que trabajan 8 empleados (4 por la mañana y 4 por la tarde)
Confeccionar un programa que permita almacenar los sueldos de los empleados agrupados en dos listas.
Imprimir las dos listas de sueldos."""



numero_veces_ingresar = int(input("Ingrese las veces que quiere ingresar los turnos: "))

saldo_matutino = []
saldo_vespertino = []
for x in range(1,numero_veces_ingresar + 1):

    valor_matutino = int(input("Ingrese el sueldo numero {} del turno matutino: ".format(x)))

    saldo_matutino.append(valor_matutino)

    valor_vespertino = int(input("Ingrese el sueldo numero {} del turno vespertino: ".format(x)))
    saldo_vespertino.append(valor_vespertino)




print("La lista del turno matutino  es de \n")
for x in range(numero_veces_ingresar):

        print(str(saldo_matutino[x]) + " ")

print("La lista del turno vespertino  es de \n")
for x in range(numero_veces_ingresar):

        print(str(saldo_vespertino[x]) + " ")
