def resultado():

    suma = 0
    numero = (int(input("ingrese un numero: ")))
    if numero >= 0:
        suma = suma + numero
        while numero >= 0:
            numero = (int(input("ingrese un numero ")))
            if numero >= 0:
                suma = suma + numero

        print("la suma es :", suma)
    else:
        print("debe ingresar un numero mayor o igual a 0")


resultado()
