#Problema usando for
print("================================================================================================")

print("Pide al usuario un numero entero positivo y determina si es primo usando el ciclo for")

print("================================================================================================")

numero = int(input("Ingrese el numero"))
primo = True

for i in range(2,numero):
    if numero % i ==0:
        print("No es primo",i,"es divisor")
        primo=False
        break
if primo:
    print("Es primo")