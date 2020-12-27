#!/usr/bin/env python3  
#-*- coding: utf-8 -*-

def imprimir(paises):
    for clave in paises:
        print(clave, paises[clave])

#MAIN BLOCKL

paises={"argentina":40000000, "españa":46000000, "brasil":190000000, "uruguay": 3400000}
imprimir(paises)
