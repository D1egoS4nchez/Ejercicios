#!/usr/bin/env python3


""" Desarrollar una funcion que reciba un string como parametro y nos muestre la cantidad de vocales. Llamarla desde el bloque principal del programa 3 veces con string distintos. """



def strings():

    lista_oracion = []
    contador_lista = []
    for x in range(3):
        oracion = input("Ingrese su oracion numero {}: \n".format(x+1))
        lista_oracion.append(oracion)
    #print(lista_oracion) 

    contador = 0
    
    for k in range(len(lista_oracion)):
        for x in range(len(lista_oracion[k])):
            if lista_oracion[k][x] == "a" or lista_oracion[k][x] == "e" or lista_oracion[k][x] == "i" or lista_oracion[k][x] == "o" or lista_oracion[k][x] == "u":
                contador += 1
        #Se guarda en una lista cada valor de cada contador pero este en el primer for para que se guarden como 3 objetos diferentes;)
        contador_lista.append(contador)
    

    print(contador_lista)
    
#Main                   
strings()







