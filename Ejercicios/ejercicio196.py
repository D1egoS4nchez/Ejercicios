#!/usr/bin/env python3
#-*- coding: utf-8 -*-

"""
Confeccionar una clase que administre una agenda personal. Se debe almacenar el nombre de la persona, teléfono y mail
Debe mostrar un menú con las siguientes opciones:
1- Carga de un contacto en la agenda.
2- Listado completo de la agenda.
3- Consulta ingresando el nombre de la persona.
4- Modificación de su teléfono y mail.
5- Finalizar programa.
"""


class Administracion:
    

    def __init__(self):
        self.menu()

    def menu(self):
        self.diccionario = {}
        puntero = 0
        while puntero != 5:
            print("1 - Cargar un contacto en la agenda")
            print("2 -  Listar completa la agenda")
            print("3 - Consulta ingresando el nombre de la persona")
            print("4 - Modificar telefono y su mail")
            print("5 - Finalizar programa")
            if puntero == 1:
                self.cargar()
            elif puntero == 2:
                self.listar()
            elif puntero == 3:
                self.consulta()
            elif puntero == 4:
                self.modificacion()
            puntero = int(input("Ingrese el punto que quiere ejecutar: "))           



    def cargar(self):
        s = "s"
        liste = []
        while s == "s" or s == "S" or s == "SI":
            nom = input("Ingrese el nombre de la persona: ")
            telefono = int(input("Ingrese el telefono de {}: ".format(nom)))
            mail = input("Ingrese su correo electronico:")
            liste.append((telefono, mail))
            self.diccionario[nom]=liste
            s = input("¿Quiere ingresar otro contacto? [s/n]")
        print("_______________________________________________")

    def listar(self):
        for nombre in self.diccionario:
            print(nombre, self.diccionario[nombre][0], self.diccionario[nombre][1])
        print("__________________________________________________")
    
    
    def consulta(self):
   

    
agenda1 = Administracion()
