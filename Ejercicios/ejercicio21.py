# -*- coding: UTF-8 -*-


""" Realizar un programa que
pida cargar una fecha cualquiera, luego verificar si dicha fecha corresponde a Navidad"""
dia_navidad = 25
mes_navidad = 12
dia = int(input("Ingrese la fecha que desee: \n"))
mes = int(input("Ingrese el mes que desee: \n"))
ano = int(input("Ingrese el año que desee: \n"))

"""def fecha():
    print("El " + str(dia) + " del mes " + str(mes) + " del año " + str(ano))

if dia == dia_navidad and mes == mes_navidad:
    print("La fecha que ingreso, se marca que es Navidad\n")
    fecha()

else:
    fecha() """

if dia >= 32 or mes >=13:
    print("No se adminte esta fecha, tiene una dato incorrecto o incoherente ")
else:
    lado = int(input("Prueba"))
