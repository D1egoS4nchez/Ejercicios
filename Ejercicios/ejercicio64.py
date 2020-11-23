#!/usr/bin/env python3
# -*- coding: utf-8 -*-


email = input("INgrese su email: ")

cantidad = 0

x = 0

while x < len(email):
    if email[x]=="@":
        cantidad += 1
    print("Itera")
    x += 1

if cantidad == 1:
    print("Correcto")
else:
    print("Incorrecto")
