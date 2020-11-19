 ## Se ingresa el primer valor

def condicion_valores(valor_funcion):
    num1 = int(input("Ingrese el primer valor: \n"))

    ## Se ingresa el segundo valor.
    num2 = int(input("Ingrese el segundo valor: \n"))

    ## Se ingresa el ultimo valor que es el tercero.
    num3 = int(input("Ingrese el tercer valor:  \n"))


 ## Se hace una funcion para mas comodidad
    if num1 > num2 and num1 > num3: ## Se pone como operador logico el "and"
        print("Pues el numero uno es el mayor \n")
        num1
    else: ## Si no se encuentra el primer numero, pasa a la siguiente condicion
        if num2 > num3:
            print("El numero dos es el mayor \n")
            print(num2)
        else:
            print("El numero tres es el mayor \n")
            print(num3)

    valor_funcion = valor_funcion + num3

    print (valor_funcion)


variable = condicion_valores(12)
