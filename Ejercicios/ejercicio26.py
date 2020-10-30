#!/usr/bin/env python3
# -*- coding: UTF-8 -*-


""" De un operario se conoce su sueldo y los años de antigüedad. Se pide confeccionar un programa que lea los datos de entrada e informe:
a) Si el sueldo es inferior a 500 y su antigüedad es igual o superior a 10 años, otorgarle un aumento del 20 %, mostrar el sueldo a pagar.
b)Si el sueldo es inferior a 500 pero su antigüedad es menor a 10 años, otorgarle un aumento de 5 %.
c) Si el sueldo es mayor o igual a 500 mostrar el sueldo en pantalla sin cambios. """


sueldo = int(input("Ingrese su sueldo: \n"))

años_antiguedad = int(input("Ingrese sus años de antigüedad(rango 0-70 años)"))

def checar_sueldo_Y_anos():
    if sueldo < 500 and años_antiguedad >= 10:
        print("Se la aumentara 20%,quedaría asi: \n")
        porcentaje = sueldo * .20
        aumento = sueldo + porcentaje
        print(porcentaje)
    else:
        if sueldo < 500 and años_antiguedad <= 5:
            print("Se la aumentara 5%,quedaría asi: \n")
            porcentaje = sueldo * .5
            aumento = sueldo + porcentaje
            print(porcentaje)

        else:
            if sueldo >= 500:
                print("Su sueldo es: \n", sueldo)


def esta_bromeando():
    if años_antiguedad >= 71:
        print("No bromee:)") 


esta_bromeando()
