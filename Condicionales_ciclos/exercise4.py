# 4. Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere calcular de forma automática el precio que debe cobrar a sus clientes por entrar. El programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada. Si el cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y 18 años debe pagar $2.000 y si es mayor de 18 años, $3.500.
import time
try:

    # Solicita al usuario ingresar su edad
    edad = int(input("Digite su edad: "))
    # Verifica el costo segun la edad ingresada
    if edad < 4:
        costo = 0
    elif edad < 18:
        costo = 2000
    else:
        costo = 3500

    # Muestra por pantalla la respuesta verificion del costo
    print("La entrada para usted tiene un costo de",costo)
# Manejo de errores en caso de que se ingrese caracteres erroneos
except ValueError:
    print("Edad ingresa incorrecta")