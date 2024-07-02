print("==============================================================================")

print("Pide al usuario un numero entero y suma sus digitos usando un ciclo while")

print("===============================================================================")

numero = 0
suma = 0
limite = 0
while numero>= 0:
    print(numero)
    numero = numero + int(input("Ingrese el numero para sumar:"))
    suma = suma + numero
    if numero >= limite:
        break
    elif numero<= limte:
        continue
    
print(f"{numero}< limite")
print(f"la suma_total es dea: {suma}")

