#!/usr/bin/env python3
# -*- coding: utf-8 -*-


nombre = input("Ingrese su nombre: ")
if nombre[0] == "a" or nombre[0] == "e" or nombre[0] == "i" or nombre[0] == "o" or nombre[0] == "u":
    print("El nombre ingresado inicia con una vocal")
else:
    print("El nombre que se ingreso no inicia con ninguna vocal")