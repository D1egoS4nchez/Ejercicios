# -*- coding: UTF-8 -*-

""" Se ingresan por teclado tres números, si al menos uno de los valores ingresados
es menor a 10, imprimir en pantalla la leyenda "Alguno de los números es menor a diez". """
numero1 = int(input("Ingrese el primer valor: \n"))
numero2 = int(input("Ingrese el segundo valor: \n"))
numero3 = int(input("Ingrese el tercer valor: \n"))

""" if numero1 >= numero2 or numero1 >= numero3:
    if numero1 >= numero2 and numero1 >= numero3:
        print("El numero uno es el mayor")
    else:
        if numero2 > numero1 or numero2 > numero3:
            if numero2 > numero1 and numero2 > numero3:
                print("El numero dos es el mayor")

if numero3 > numero1 or numero3 > numero2:
    if numero3 > numero1 and numero3 > numero2:
        print("El numero 3 es el mayor") """
def ver_Numero(): # Funcion para determinar cual numero es el menor
    if numero1 > numero2 and numero1 > numero3:
        if numero2 < numero3:
            print("El numero 2 es el menor")
        else:
            print("El numero 3 es el menor ")

    if numero2 > numero1 and numero2 > numero3:
        if numero1 < numero3:
            print("El numero 1 es el menor")
        else:
            print("El numero 3 es el numero menor ")

    if numero3 > numero1 and numero3 > numero2:
        if numero2 < numero1:
            print("El numero 2 es el menor")
        else:
            print("El numero 1 es el numero menor ")

def basica(): #Funcion en la que solo se sabe que alguno de ellos es menor 
    if numero1 < 10 or numero2 < 10 or numero3 < 10:
        print("Alguno de estos numeros es menor a 10")
ver_Numero()
