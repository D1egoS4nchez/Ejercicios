#!/usr/bin/env python3  
#-*- coding: utf-8 -*-

""" Crear un diccionario en Python que defina como clave el número de documento de una persona y como valor un string con su nombre.
Desarrollar las siguientes funciones:
1) Cargar por teclado los datos de 4 personas.
2) Listado completo del diccionario.
3) Consulta del nombre de una persona ingresando su número de documento. """


#Funcion para cargar un diccionario como el numero como la clave y el nombre como valor ;)
def cargar():
    #Creamos un diccionario vacio
    diccionario = {}
    # Un puntero para luego modificarlo en la funcion while
    whil = "s"
    #Esta nos dice que mientras la variable whil sea s este ppodria continuar y hacer lo siguiente
    while whil == "s" or  whil == "S"  or whil == "si":

        #Preguntamos en las variables algunas cosas, estos son los datos que vamos a guardar
        num_doc = int(input("Ingrese el numero de documento de la persona: "))
        nombre = input("Ingrese el nombre de una persona")
        #Agregamos la llave y el valor al diccionario
        diccionario[num_doc]=nombre
        #Sobreescribimos los valores con una entrada para que a la hora de modificar la variable y se devuelva al while se vea si se cumple la condicion del while, si no es asi este no hace el while
        whil = input("Quiere ingresar otro numero y nombre?: [s/n]")
    #Se retornar el diccionario que le agregamos en cada vuelta si se cumplio lo del while
    return diccionario


#Funcion para lista las claves y los valores de los diccionarios, en esta la ingresamos como parametro el diccionario
def listado(dic):
    #Imprimimos esta frase para tenerla segmentada pero no vale para pura madre
    print("Numero / Nombre")
    #Un bucle para iterar en cada clave e imprimir la clave y el valor
    for x in dic:
        #Imprimimos lo que es la clave y el valor y los separamos con un /
        print(x, dic[x], sep="/",)
    
#Funcion para checar el nombre ingresandole un valor, en este caso un entero
def checada(dic):
    #Ingresamos el valor que queremos entrar, en este le podemos poner un ciclo for con una variable que tenga el numero de veces que vamos a hacer la busquedad o tambien un while, igual que en la
    #funcion cargar para que sea continuo
    nro = int(input("Ingrese el numero de documento a consultar: "))
    #Esta funcion dice que si el numero ingresamos esta en el diccionario, que haga lo siguiente
    if nro in dic:
        #Si se cumple la condicion este imprimira lo que es el valor ya que ingresamos la clave
        print("Nombre de la persona:",dic[nro])
    #Si no este imprimira un mensaje negativo
    else:
        print("No existe una persona con dicho numero de documento")



#MAIN BLOCK

dic = cargar()
listado(dic)
checada(dic)
