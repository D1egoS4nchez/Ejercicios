#!/usr/bin/env python3
#-*- coding: utf-8 -*-

#----------------------------------------------------------------------------------------------------------------------

#Abrimos el documento y lo ponemos como pos_f
def opens_pos():
    positive_words = []
    with open("positive_words.txt", "r") as pos_f:
        #Iteramos en cada linea del documento
        for lin in pos_f:
            #Checamos si el primer caracter sea diferente a ; y a un salto de linea
            if lin[0] != ";" and lin[0] != "\n":
                #Si cumple la condicion anterior, este va a agregar a la lista la linea y la va a separar
                
                positive_words.append(lin.strip())

    #Retornamos una lista con palabras positivas
   return positive_words
#---------------------------------------------------------------------------------------------------------------------

#Funcion para separa caracteres de puntuacion 

def strip_punctuation(string):
    #Lista de caracteres
    punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
    #Iteramos en cada letra en la cadena que ingresamos como parametro en la funcion "strip_punctuation"
    for letra in string:
        #Checamos si la letra de la vuelta esta en la lista "punctuation_chars", va hacer lo siguiente
        if letra in punctuation_chars:
            #Sobreescribimos en la cadena y reemplazamos la letra en la cadena y la remplazamos
            string = string.replace(letra, "")
    print(string)
    #Retornamos la string que se ingreso sin signos
    return string
#--------------------------------------------------------------- N E G A T I V E -- W O R D S ------------------------
def opens_neg():
    #Hacemos una lista vacia para palabras negativas
    negative_words = []
    #Abrimos el archivo y ponemos como neg_f para acceder a el
            #Si da un error, eliminar "r" en las dos funciones de abrir
    with open("negative_words.txt", "r") as neg_f:
        #Iteramos en cada linea del documento
        for lin in neg_f:
            #Checamos las siguientes condiciones
            if lin[0] != ";" and lin[0] != "\n":
                #Si se cumple, vamos a agregar la linea pero quitamos los espacios vacios
                negative_words.append(lin.strip())
    return negative_words

#----------------------------------------------------------------------------------------------------------------------

#Funcion para obtener las letras que hay en la cadena que vamos a ingresar como parametro pero viendo si esta en la lista de palabras negativas
def get_neg(z):
    #Inicializamos una variable para acumular 
    count = 0
    #Hacemos una variable negative_words, esta va a guardar lo que retorne de la funcion opens_neg
    negative_words = opens_neg()
    #Guardamos una variable lo que es la cadena pero esta sin ningun signo especial
    x = strip_punctuation(z)
    #Guardamos en una variable lo que es la cadena en la variable anterior, pero esta se convierte en minusculas y se separa cada una de ellas
    o = x.lower().split()
    #Iteramos en cada una de las palabras de la lista o
    for w in o:
        #Si la palabra se encuentra en la lista que guardamos en la variable negative words, va a agregar un valor a la variable count
        if w in negative_words:
            count += 1
    #Retornamos el valor del count para asi despues acceder a el
    return count
#----------------------------------------------------------------------------------------------------------------------
def get_pos(z):
    count = 0
    positive_words = opens_pos()
    x = strip_punctuation(z)
    o = x.lower().split()
    for w in o:
        if w in positive_words:
            count += 1
    return count
#----------------------------------------------------------------------------------------------------------------------    
# VER Y AGREGAR VALORES PARA EL CSV ----------------------------------------------------------------------------------
def write_file():
    with open("resulting_data.csv", "w")as pf:
        a = ["Number of Retweets", "Number of Replies", "Positive Score"]
        
def read_file(
