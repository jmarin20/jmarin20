def sumaPrimos():
    suma = 0
    for i in range(0,30):
        num = int(input("inserta un numero: "))

        if num != 1:
            for i in range(2, num):

                if (num % i) == 0:
                    # no es primo
                    break
            else:
                suma = suma + num

    print("la suma total es de",suma)


sumaPrimos()