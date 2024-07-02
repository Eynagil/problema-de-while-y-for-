# Problemas usando for
print("========================================================================================================")

print("Pide al usuario un nuero entero positivo NNN y suma los primeros NNN numeros naturales usando el ciclo for")

print("=======================================================================================================")

print("Ingrese el valor final (N)")
a = int(input())
b = 0
for i in range(1, a+1):
    print(i)
    b=b+i
print("La suma es: ",b)