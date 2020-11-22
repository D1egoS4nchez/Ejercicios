#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Escribir un programa que pida ingresar coordenadas (x,y) que representan puntos en el plano.
Informar cuántos puntos se han ingresado en el primer, segundo, tercer y cuarto cuadrante. Al comenzar el programa se pide que se ingrese la cantidad de puntos a procesar."""

total_coordenadas = int(input("Ingrese cuantos pares de coordenadas quiere meter: \n"))


total_coordenadas += 1

for f in range(1, total_coordenadas):
    x_coordenada = int(int("Ingrese la coordenada X del par numero {}: ".format(f)))

    y_coordenada = int(int("Ingrese la coordenada Y del par numero {}: ".format(f)))

    if x_coordenada ==
