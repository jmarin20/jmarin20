print ("leer una secuencia de 30 numeros y mostrar la suma y el producto de ellos")

def sumProd():
    suma = 0
    producto = 1

    for i in range(0, 30):
        num = int(input("ingrese un numero: "))
        suma = suma + num
        producto = producto * num

    print("la suma de los numeros es: ", suma)
    print("el producto de los numeros es:", producto)


sumProd()

