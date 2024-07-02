# problema usando for 1
print("============================================================")

print("pide al usuario un numero entero positivo y muestra su tabla de multiplicar del 1 al 10 usando un ciclo for")

print("=============================================================")

tabla_desde = 1
tabla_hasta = 10
desde = 1
hasta = 10

for factor1 in range(tabla_desde, tabla_hasta + 1):
    print(f"Tabla de multipilicar del {factor1}:")
    for factor2 in range(desde, hasta + 1 ):
        print(f"{factor1} x {factor2} = {factor1 * factor2}")
    print()