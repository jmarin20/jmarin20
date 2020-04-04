def MostrarPares():

    contadorPares = 0
    lista = []

    while True:
        numero = int(input("Ingrese un numero: "))
        if numero % 2 == 0:
            lista.append(numero)
            contadorPares = contadorPares+1
            if contadorPares==30:
                break
        else:
            continue

    print("Los pares ingresados son: ")
    print(lista)


MostrarPares()