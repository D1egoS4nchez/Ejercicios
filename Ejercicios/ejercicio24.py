# -*- coding: UTF-8 -*-

""" Se ingresan tres valores por teclado, si todos son iguales se imprime la suma del primero con el segundo y
a este resultado se lo multiplica por el tercero. """

numero1 = int(input("Ingrese el primer valor: \n"))
numero2 = int(input("Ingrese el segundo valor: \n"))
numero3 = int(input("Ingrese el tercer valor: \n"))


if numero1 == numero2 and numero2 == numero3 and numero1 == numero3:
    print("Son iguales")
    resultado = (numero1 + numero2) * numero3
    print(resultado)
