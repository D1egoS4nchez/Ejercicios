#!/usr/bin/env python3  
#-*- coding: utf-8 -*-

"""
Desarrollar un programa que cargue los lados de un triángulo e implemente los siguientes métodos: inicializar los atributos, 
imprimir el valor del lado mayor y otro método que muestre si es equilátero o no. El nombre de la clase llamarla Triangulo.
"""

class Triangulo:
    def inicializar(self):
        lista = []
        for x in range(3):
            valor = float(input("Ingrese el valor del lado:"))
            lista.append(valor)
        self.lados = lista

    def imprimir(self):
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
