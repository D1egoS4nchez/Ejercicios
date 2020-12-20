#!/usr/bin/env python3
#-*- coding: utf-8 -*-


"""
En una empresa se almacenaron los sueldos de 10 personas.
Desarrollar las siguientes funciones y llamarlas desde el bloque principal:
1) Carga de los sueldos en una lista.
2) Impresión de todos los sueldos.
3) Cuántos tienen un sueldo superior a $4000.
4) Retornar el promedio de los sueldos.
5) Mostrar todos los sueldos que están por debajo del promedio. """

def cargar_lista():
    lista = []
    for x in range(10):
        valorsto = int(input("Ingrese el sueldo que quiere que tenga la cara de pija: "))
        lista.append(valorsto)
    print("Todos lo sueldos son estos: \n {} ".format(lista))
    return lista


def checar_sueldo(lis):
    contador = 0
    for x in range(len(lis)):
        if lis[x] > 4000:
            contador += 1
    return contador

def promedio(lis): 
    suma = 0
    for x in range(len(lis)):
        suma = suma + lis[x]
    promedio = suma / 10
    return promedio

def debajo_promedio(prom, lis):
    debajo = 0
    lista_valor = []
    for x in range(len(lis)):
        if lis[x] < prom:
            debajo += 1
            lista_valor.append(lis[x])
    return debajo, lista_valor


def

#MAIN BLOCK

lista = cargar_lista()
contador = checar_sueldo(lista)
promedio = promedio(lista)
print("El promedio de los sueldos ingresados son: {}".format(promedio))
debajo_del_promedio, valores = debajo_promedio(promedio, lista)
#Se muestra los sueldos que estan debajo del promedio 

print("Los sueldos que estan debajo del promedio hay {}".format(debajo_del_promedio))

print(valores)
