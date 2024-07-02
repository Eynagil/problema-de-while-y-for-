print("==============================================================================================")

print("pide al usuario un numero entero positivo y muestra sus multiplos del 1 al 10 usando un ciclo while")

print("================================================================================================")

tabla = float(input("Escribe la tabla que quieras ver:"))
comienzo = 1
while comienzo <= 10:
    resultado = tabla * comienzo
    print(f"{tabla} * {comienzo} = {resultado}")
    comienzo +=1