#!/usr/bin/env python3
#-*- coding: utf-8 -*-

#Clase Cliente para cada objeto que sea cliente
class Cliente:
    
    #Metodo init, en este ponemos como parametro el nombre que le vamos a poner 
    def __init__(self,nombre):
        #Haceos un atributo llamado nombre con el valor que le ingresemos en el parametro
        self.nombre = nombre
        #Incializamos el atributo monto con valor 0 
        self.monto = 0

    #Metodo depositar, en este tiene como parametro el valor que le vamos a agregar
    def depositar(self,monto):
        #Con el valor que inicializamos en el metodo init, agregamos el valor que pusimos como parametro, este se va sobreescribir y se va a guardar
        self.monto = self.monto + monto

    
    def extraer(self,monto):
        self.monto = self.monto - monto

    def retornar_monto(self):
        return self.monto

    def imprimir(self):
        print(self.nombre, "tiene depositado la suma de",self.monto)


#Clase que se llama Banco* este hace objetos y pone sus metodos de la clase anterior
class Blanco:
    
    #Metodo init, en este se inicializan varios objetos que son del cliente1 al cliente3, pero en este caso ponemos los objetos que se guien con la clase
    #Cliente que es aparece ahi, en este caso esta diciendo que se aplique la clase cliente en este objeto y todos sus metodos, segun como lo mandemos a llamar
    def __init__(self):
        #Hacemos el objeto cliente1 y ponemos la clase Cliente con el parametro que requiere, en este caso el nombre
            #Juan
        self.cliente1 = Cliente("Juan")
            #Ana
        self.cliente2 = Cliente("Ana")
            #Diego
        self.cliente3 = Cliente("Diego")

    #EL metodo operar a los objetos clientes y utiliza los metodos de su clase que en este caso el metodo es depositar
    def operar(self):
        #Funciona de la siguiente manera, este toma el objeto ya antes inicializado con la clase Cliente y agarra el metodo de esta clase y ingresa su parametro, este parametro
        #   se guarda en la variable local monto de su objeto osea del cliente.
        self.cliente1.depositar(100)
        self.cliente2.depositar(150)
        self.cliente3.depositar(300)
        #En este metodo llamado extraer lo que se toma es la variable monto del objeto y extrae lo que se ingreso en el parametro del metodo
        self.cliente3.extraer(150)

    #Metodo que se encarga de imprimir y obtener el total
    def depositos_totales(self):
        #Se guarda en la variable total lo que se tiene de monto, en este caso el metodo retornar monto de cada objeto y lo suma
        total = self.cliente1.retornar_monto() + self.cliente2.retornar_monto() + self.cliente3.retornar_monto()

        print("El total de dinero del banco es: ",total)
        #Se usa el metodo imprimir de la clase Cliente para imprimir los valores del objeto que estan asignados y guardados para cada objeto
        self.cliente1.imprimir()
        self.cliente2.imprimir()
        self.cliente3.imprimir()


# bloque principal        

banco1=Blanco()
banco1.operar()
banco1.depositos_totales()
