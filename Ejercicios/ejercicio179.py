#!/usr/bin/env python3  
#-*- coding: utf-8 -*-

import random

dado1 = random.randint(1,6)
dado2 = random.randint(1,6)

print("Primer dado: {}".format(dado1))
print("Segundo dado: {}".format(dado2))
suma = dado1 + dado2
if suma == 7:
    print("Gano")
else:
    print("Perdio")
