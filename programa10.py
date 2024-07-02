print("======================================================================================================")

print("Escribe un programa que simule un cajero automatico. Pide al usuario que ingrese su PIN y permite tres intento para ingresar correctamente.")

print("========================================================================================================")

PIN = 4475
intento = 0
limite = 3

while intento<limite:
    Numero = int(input("Ingrese el nuemro clave"))
    if Numero==PIN:
        print("Su contraseña es valida")
        break
    elif Numero!=PIN:
        intento+=1
        print("PIN es incorrecto")
    if intento==limite:
        print("Su tarjeta a sido bloqueada")