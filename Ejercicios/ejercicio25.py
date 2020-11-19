# -*- coding: UTF-8 -*-


#Indicaciones

""" Escribir un programa que pida ingresar la coordenada de un punto en el plano, es decir dos valores enteros x e y (distintos a cero).
Posteriormente imprimir en pantalla en que cuadrante se ubica dicho punto. (1º Cuadrante si x > 0 Y y > 0 , 2º Cuadrante: x < 0 Y y > 0, etc.) """
def punto_Plano():
    puntoX = int(input("Ingrese el punto X \n"))

    puntoY = int(input("Ingrese el punto Y  \n"))

    angulo_Cuadrante = int(input("Ingrese el angulo para saber el cuadrante \n"))

    print("La coordenada es", puntoX , puntoY)

    if angulo_Cuadrante >= 0 and angulo_Cuadrante < 90:
        print("El angulo esta en el primer cuadrante")
    else:
        if angulo_Cuadrante >= 90 and angulo_Cuadrante < 180:
            print("El angulo esta en el segundo cuadrante")
        else:
            if angulo_Cuadrante >= 180 and angulo_Cuadrante <= 270:
                print("El angulo esta en el tercer cuadrante")
            else:
                if angulo_Cuadrante >= 270 and angulo_Cuadrante <= 360:
                    print("El angulo esta en el cuarto cuadrante")
                else:
                    print("El angulo tiene mas vueltas")

punto_Plano()
