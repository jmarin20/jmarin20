primerNumero = int(input("ingrese Primer Numero: "))
segudnoNumero = int(input("ingrese Segundo Numero: "))
n = primerNumero + 1
resultado = 0
for i in range(1, n):
    resultado = resultado + segudnoNumero
    print(resultado)

print(f"El resultado es:  {resultado}")