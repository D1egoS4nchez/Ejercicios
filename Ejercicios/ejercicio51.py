#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""" Realizar un programa que lea los lados de n triángulos, e informar:
a) De cada uno de ellos, qué tipo de triángulo es: equilátero (tres lados iguales), isósceles (dos lados iguales), o escaleno (ningún lado igual)
b) Cantidad de triángulos de cada tipo."""


equilatero = 0
isoceles = 0
escaleno = 0

n_triangunlos = int(input("Ingrese el numero de triangulos que quiere meter: \n"))



n_triangunlos += 1
for f in range(1,n_triangunlos):

    lado_1 = int(input("Ingrese el lado 1 del triangulo {}: \n".format(f)))


    lado_2 = int(input("Ingrese el lado 2 del triangulo {}: \n".format(f)))


    lado_3 = int(input("Ingrese el lado 3z del triangulo {}: \n".format(f)))

    if lado_1 == lado_2 and lado_1 == lado_3:
        equilatero += 1
    else:iuf
        escaleno += 1
    if lado_1 == lado_2 or lado_1 == lado_3 or lado_2 == lado_3:

        isoceles += 1


print(equilatero)
print(escaleno)
