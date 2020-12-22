#!/usr/bin/env python3
#-*- coding: utf-8 -*-

"""Desarrollar una función que solicite la carga del dia, mes y año y almacene dichos datos en una tupla que luego 
debe retornar. La segunda función a implementar debe recibir una tupla con la fecha y mostrarla por pantalla."""

def cargar_fecha():
    dd = int(input("Ingrese el numero de dia: "))
    mm = int(input("Ingrese el numero de mes: "))
    aa = int(input("Ingrese el numero del año: "))
    return(dd, mm, aa)

def imprimr(fecha):
    print(fecha[0], fecha[1], fecha[2], sep="/")

#MAIN BLOCK

tuplas = cargar_fecha()
imprimr(tuplas)
