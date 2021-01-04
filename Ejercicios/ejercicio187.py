#!/usr/bin/env python3
#-*- coding: utf-8 -*-

"""Implementar una clase llamada Alumno que tenga como atributos su nombre y su nota. Definir los métodos para inicializar sus atributos, imprimirlos y mostrar un mensaje si está regular (nota mayor o igual a 4)

Definir dos objetos de la clase Alumno."""

class Alumno:

    def inicializar(self, nombre, nota):
        self.nombre=nombre
        self.nota=nota

    def imprimir(self):
        print("Nombre: {} / Nota: {}".format(self.nombre,self.nota))
        
    def mostrar_estado(self):
        if self.nota < 4:
            print("El alumno {} tiene una nota regular".format(self.nombre))
        else:
            print("El alumno {} tiene una nota libre".format(self.nombre))


#MAIN BLOCK

alumno1 = Alumno()
alumno1.inicializar("Diego",2)
alumno1.imprimir()
alumno1.mostrar_estado()

alumno2 = Alumno()
alumno2.inicializar("Pedro", 9)
alumno2.imprimir()
alumno2.mostrar_estado()

