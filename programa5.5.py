#Problema usando for
print("=================================================================================================================")

print("Pide al usuario un numero entero positivo y muestra todos los numeros impares 1 hasta ese numero usando un ciclo for")

print("=================================================================================================================")

inicio = int(input("Indicame el numero inicial:"))
fin = int(input("Indicame el nuemro final:"))
print("Te muestro los numeros imparares del intervalo /n")
for i in range(inicio,fin + 1):
    if i % 2 !=0:
        print(i)