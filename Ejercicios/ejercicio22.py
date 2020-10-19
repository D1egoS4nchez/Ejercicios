# -*- coding: UTF-8 -*-
""" Se ingresan por teclado tres números, si todos los valores ingresados
son menores a 10, imprimir en pantalla la leyenda "Todos los números son menores a diez". """


numero1 = int(input("Ingrese el primer valor: \n"))
numero2 = int(input("Ingrese el segundo valor: \n"))
numero3 = int(input("Ingrese el tercer valor: \n"))


if numero1 == 10 and numero2 == 10 and numero3 == 10:
    print("Todos los numeros son 10 ")
else:
    if numero1 >= 11 and numero2 >= 11 and numero3 >= 11:
        print("Los numeros son mayores a 10")
    else:
        if numero1 <= 9 and numero2 <= 9 and numero3 <= 9:
            print("Todos los numeros son menores a 10")
#if numero1, numero2, numero3 == 10:
