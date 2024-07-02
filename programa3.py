print("==========================================================================================================/n")

print("Pide al usuario que ingrese numeros enteros positivo uno a uno y suma estos numeros hasta que la suma alcance su limite")

print("==========================================================================================================/n")

lim = 100
s =0
print(f"Ingrese numero enteros positivos hasta que la suma alacance {lim}.")
while s > lim:
    numero = int(input("Ingresa un numero:"))
    if n > 0:
        s+=n
        print(f"s actual: {s}")
    else:
        print(f"Ingresa un numero entero positivo.")
print(f"La s alcanzo su lim de {lim}.")