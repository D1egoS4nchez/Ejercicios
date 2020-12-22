#!/usr/bin/env python3
#-*- coding: utf-8 -*-


"""Confeccionar una función que reciba entre 2 y 5 enteros. 
La misma nos debe retornar la suma de dichos valores. Debe tener tres parámetros por defecto."""

def sumar(v1=0, v2=0, v3=0, v4=4, v5=7):
    suma = v1+v2+v3+v4+v5
    return suma


print(sumar(5,3,1,5))
