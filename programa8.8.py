print("====================================================================================================")

print("Pide al usuario un rango de temperatura en gradso celsius (inicio y fin) y muestra la conversion a Fahrenheit para cada rango usando el ciclo for")

print("======================================================================================================")

inicio = int(input("Ingrese el grado de inicio de celsius: "))
fin = int(input("Ingrese el grado de fin de celsius: "))
print("convertir de celsius a fahrenheit:")
for celsius in range(inicio,fin +1):
    
    fahrenheit = (celsius*9/5) + 32
print(f"{celsius} en grados celsius es {fahrenheit} en grados fahrenheit.")