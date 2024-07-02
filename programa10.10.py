print("=======================================================================================================")

print("Pide al usuario una cadena de texto y un numero entero positivo NNN. Muestra la cadena repetida NNN  veces, cada vez en una nueva linea, usando el ciclo for")

print("=======================================================================================================")

texto = input("Ingrese una palabra")
numero = int(input("Ingrese un numero entero positivo:"))
for i in range(1, numero+1):
    print(texto)