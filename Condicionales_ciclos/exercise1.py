"Escribir un programa que pida al usuario un numero entero y muestre en pantalla si es para o no"
try:
    # Solicita al usuario ingresar un número entero
    num = int(input("Ingrese un numero: "))

    # Verifica si el numero ingresado es pas
    par = ("No es par")
    if num % 2 == 0:
        par = ("Es par")
    # Muestra por pantalla si el numero es par
    print(par)
    # Manejo de errores en caso de que se ingrese caracteres erroneos
except ValueError:
    print("Error")
    
