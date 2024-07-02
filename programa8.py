print("==========================================================================================")

print("Pide al usuario un numero entero positivo y cuenta cuantos digito tiene usando un ciclo while")

print("==========================================================================================")
numero = int(input("Estimado usuario ingrese un nuemro entero: "))
contador_digitos = 0
if numero == 0:
    contador_digitos = 1
else:
    numero = abs(numero)
    print(numero)
    while numero > 0:
        numero = numero // 10
        contador_digitos += 1
print(f"El resultado es", contador_digitos, "dígitos.")