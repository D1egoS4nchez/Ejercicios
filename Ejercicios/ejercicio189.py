#!/usr/bin/env python3  
#-*- coding: utf-8 -*-

"""
Desarrollar un programa que cargue los lados de un triángulo e implemente los siguientes métodos: inicializar los atributos, 
imprimir el valor del lado mayor y otro método que muestre si es equilátero o no. El nombre de la clase llamarla Triangulo.
"""
#Se hace la clase Triangulo 
class Triangulo:

    #Hacemos el primer metodo que es para inicializar los valores
    def inicializar(self):
        #Hacemso una lista vacia
        lista = []
        #Se hace un for para ingresar en la lista tres valores
        for x in range(3):
            #Ingresamos en la variable valor el valor que queramos
            valor = float(input("Ingrese el valor del lado:"))
            #Agregamos a la lista el valor que acabamos de ingresar
            lista.append(valor)
        #Hacemos el atributo lado y en este le agregamos la lista
        self.lados = lista

    def imprimir(self):
        s = input("¿Quiere ver su lados impresos verticalmente? [s/n]")
        if s == "s" or s == "S" or s == "si":
            for elemento in self.lados:
                print(elemento)
        else:
            print(self.lados)
    def checar(self):
        if self.lados[0] == self.lados[1] and self.lados[0] == self.lados[2]:
            print("Es equilatero")
        else:
            print("No es equilatero")
    
def main():
    lista_lados = Triangulo()
    lista_lados.inicializar()
    lista_lados.imprimir()
    lista_lados.checar()

main()
