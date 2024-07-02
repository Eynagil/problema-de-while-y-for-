# problema usando for
print("===========================================================================================================")

print("Pide al usuario que ingrese una cadena de texto y cuenta cuantas vocales hay en la cadena de usando el ciclo for")

print("==========================================================================================================")

def cuentaVocales(texto):
    vocales = "aeiou"
    contador = 0
    longitud = len(texto)
    
    for i in range(longitud):
        letra = texto.lower()[i]
        print(letra)
        if letra in vocales:
            contador += 1
    return contador

texto = input("Ingrese un texto: ")
contador = cuentaVocales(texto)
print(f"El numero de vocales de la cadena {texto} es igual a {contador}")