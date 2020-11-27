#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Cargar por teclado y almacenar en una lista las alturas de 5 personas (valores float)
Obtener el promedio de las mismas. Contar cuántas personas son más altas que el promedio y cuántas más bajas."""

suma = 0
promedio_mas = 0

promedio_menos= 0
for x in range(1,5+1):
    lista_alturas = float(input("Ingrese las alturas de las personas"))
