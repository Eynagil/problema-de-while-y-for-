print("=======================================================================================")

print("Pide al usuario un numero un numero entero positivo y convierte ese numero a binario usando un ciclo while")

print("=======================================================================================")

numero_decimal = int(input("Ingrese un numero entero positivo:"))
while numero_decimal <=0:
    print("Este numero es negativo debes ingresar un numero entero positivo.")
    numero_decimal=int(input("otra vez"))
    
numero_binario = ""
while numero_decimal>0:
    residuo = numero_decimal % 2
    numero_binario = str(residuo) + numero_binario
    numero_decimal //= 2
print(f"El numero binario equivalente es: (numero_binario)")