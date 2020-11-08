#!/usr/bin/env python3
# -*- coding: utf-8 -*-
x = 1
numero_inicial = 11
contador_pete = 0
cuenta_sietes =  0
while x <= 25:
    print("{}. El numero va es {}".format(x, numero_inicial))
    numero_inicial = numero_inicial + 11
    x = x + 1
    if numero_inicial % 2 == 0:
        contador_pete += 1
    else:
        if numero_inicial % 7 == 0:
            cuenta_sietes += 1

print("Se ha podido dividir los numeros {} veces".format(contador_pete))
print("Solo se pudieron dividir {} numeros entre 7".format(cuenta_sietes))
