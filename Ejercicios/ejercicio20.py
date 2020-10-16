# -*- coding: utf-8 -*-

##  Operador or
""" La condicion con un operador el operador or se le como O, esta va a pasar si una de las condiciones es verdadera
Si las dos o mas condiciones son falsas, esta pasara por la rama de falsa """


def ejemplos():
    print("Para ingresar los datos correctamente ponga como numero decimal, ejemplo: 1")
    print("Checar si su numero es aceptable \n")
    print("\n")
            #Se pondra una entrada input para asi saber si el numero es aceptable
    numero = int(input("Ingrese el numero: \n"))

    if numero >= 4 and numero <= 0:
        print("Su numero no es aceptable")

    return numero

ejemplos()

dia = int(input("Ingrese el nro del dia: \n"))
mes = int(input("Ingrese el nro del mes: \n"))
ano = int(input("Ingrese el nro del año: \n"))

#Condicion para los meses
def condicionMS():

    if mes >= 13:
        print("NO se admiten meses mas de 12")
    else:
        if mes == 1 or mes == 2 or mes == 3:
            print("Corresponde al primer mes trimestre del año;)")

        else:
            print("Es alguno de los meses")

# Condcion para los dias
def condicionD():
    if dia >= 16 and dia <= 1:
        print("Funciona la prueba")


condicionD()
condicionMS()
