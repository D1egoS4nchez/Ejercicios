#!/usr/bin/env python3
#-*- coding: utf-8 -*-

"""
Plantear una clase Persona que contenga dos atributos: nombre y edad. Definir como responsabilidades la carga por teclado y su impresión.
En el bloque principal del programa definir un objeto de la clase persona y llamar a sus métodos.

Declarar una segunda clase llamada Empleado que herede de la clase Persona y agregue un atributo sueldo y muestre si debe pagar impuestos (sueldo superior a 3000)
También en el bloque principal del programa crear un objeto de la clase Empleado.
"""

#Se hace la clase padre que se llama Persona

class Persona:
    
    #Inicializamos los atributos que va a tener la clase padre, que son nombre y edad 
    def __init__(self):

        self.nombre = input("Ingrese el nombre: ")
        self.edad = int(input("Ingrese la edad: "))
    
    #Imprimimos los atributos de la clase, en este caso lo que ingresemos cuando se declare el objeto va a mostrarlo

    def imprimir(self):
        print("Nombre: ",self.nombre)
        print("Edad: ",self.edad)



#Clase hija

#La herencia se presenta en la clase Empleado, en la declaración de la clase indicamos entre paréntesis el nombre de la clase de la cual hereda
class Empleado(Persona):
    

    #Metodo init
    def __init__(self):
        #Con el metodo super, agarramos de la clase padre el metodo init de el
        super().__init__()
        #Hacemos un metodo adentro de la clase empleado, pero ya hay atributos de la clase padre
        self.sueldo = float(input("Ingrese el sueldo: "))

    
    #Metodo imprimir
    def imprimir(self):
        #Se toma el metodo imprimir de la clase padr
        #Se toma el metodo imprimir de la clase padree
        super().imprimir()
        print("Sueldo: ".format(self.sueldo))

    #Hacemos un metodo que tome el atributo de la clase
    def paga_impuestos(self):
        if self.sueldo > 3000:
            print("Debe de pagar impuestos")
        else:
            print("No debe de pagar impuestos")


#MAIN BLOCK

#Se hace un objeto
persona1 = Persona()
persona1.imprimir()
print("_____________________________")

empleado1=Empleado()
empleado1.imprimir()
empleado1.paga_impuestos()

#----- No borrar ------------

#Hoy en un sueño, creo que me enamore xD, era una muchacha que no era de aquí, eran de las personas que caian y es por eso que no se pudo nada, supongo que el sentimiento era mutuo

#----- No borrar ------------


