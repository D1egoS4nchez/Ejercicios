#!/usr/bin/env python3  
#-*- coding: utf-8 -*-

#Se hace la clase con la palabra class
class Persona:
    #Despues de los dos puntos hacemos los metodos como si fueran unas funciones
    
                    #
    def inicializar(self,nom):
        self.nombre=nom

    def imprimir(self):
        print("Nombre",self.nombre)



#MAIN BLOCK

persona1 = Persona()
persona1.inicializar("Pedro")
persona1.imprimir()

persona2 = Persona()
persona2.inicializar("Carla")
persona2.imprimir()
