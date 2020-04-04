contador=int(0)
dividendo = int(input("ingrese el dividendo: "))
divisor = int(input("ingrese el divisor: "))

dividendo=dividendo-divisor
while(dividendo >= 0):
    contador=contador+1
    dividendo=dividendo-divisor
print(f"El resultado es:  {contador}")