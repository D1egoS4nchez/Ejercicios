#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Solicitar el ingreso de una clave por teclado y almacenarla en una cadena de caracteres.
Controlar que el string ingresado tenga entre 10 y 20 caracteres para que sea válido, en caso contrario mostrar un mensaje de error."""


clave_ingreso = input("Ingrese su  clave")

cantidad = len(clave_ingreso)
print(cantidad)

if cantidad >= 10 and cantidad <= 20:
    print("Es validad")

else:
    print("No es valida")
