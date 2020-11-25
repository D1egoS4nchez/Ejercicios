#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Definir por asignación una lista con 8 elementos enteros. Contar cuantos de dichos valores almacenan un valor superior a 100."""



lista_ocho_valores = [232,65,211,43,122,436,213,127]

contador = 0
for x in range(len(lista)):
    if lista_ocho_valores[x] >= 100:
        contador += 1
    else:
        print("No pa, el numero {} no es mas grande que 100".format(lista_ocho_valores[x]))
