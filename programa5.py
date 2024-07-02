print("===================================================================================================================================")

print("Escribe un programa que elija un numero alaetorio entre 1 y 10 y permita al usuario adivinarlo, dandole pista de mayor o menor hasta que acierte. usando ciclo while")

print("===================================================================================================================================")

import random
El_numero_misterioso = random.randint(1,10)
adivina = None
print("Es decir estoy pensando un numero entre 1 y 10 asi que trata de adivinar jeje")

while adivina!= El_numero_misterioso:
    adivina = int(input("escribe el nuemro:"))
    if adivina < El_numero_misterioso:
        print("intenta nuevamente")
    elif adivina > El_numero_misterioso:
        print("intenta nuevamente")
    else:
        print("GENIAL! adivinaste el numero.")