# contar hasta un numero dado

n = int(input("Ingrese un numero entero positivo"))
if n <=0:
    print("numero positivo")
else:
    contador = 1
while contador <=n:
    print(contador)
    contador += 1