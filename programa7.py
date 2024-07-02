print("===============================================================================================================================")

print("Pide al usuario que ingrese un numero positivo.Si el usuario ingresa un numero negativo,solicita nuevamente la entrada hasta que ingrese un numero postivo. Usa el ciclo while")

print("============================================================================================================================")

numero = int(input("Ingresa el numero positivo:"))

while numero <= 0:
    print("El número que ingreso es negativo.")
    numero = int(input("Ingresa un número positivo: "))

print(f"El numero que ingreso es positivo: (numero)")