# La presente actividad tiene como objetivo una calculadora que debe ser desarrollada en el
# lenguaje de programación Python. Para ello tenga en cuenta los siguientes puntos:
# 1. El ejercicio se debe desarrollar utilizando funciones. No se pueden utilizar métodos
# diferentes a append, reverse, len.
# 2. Por cada operación aritmética debe generar una función. Para la función de división
# deberá mostrar el cociente con 3 números decimales, y, el cociente entero.
# 3. Debe crear un método main o método principal en el que se incluya:
# a. La cantidad de números que el usuario desea operar (cuantos números va a
# sumar, restar, multiplicar o dividir).
# b. Debe tener el menú de opciones para que el usuario determine cuál es la
# operación aritmética que desea utilizar, además, debe incluir una opción
# para salir del programa.
# 4. Se deben visualizar los resultados de la siguiente forma:
# a. Por cada operación aritmética que se realice entre dos números se debe
# mostrar el resultado parcial y cuando se operen todos los números el
# resultado final.
numeros = []  # Lista para almacenar los números ingresados por el usuario
resultados = []  # Lista para almacenar los resultados parciales de las operaciones
def suma(a, b):
    return a + b
def resta(a, b):
    return a - b
def multiplicacion(a, b):
    return a * b
def division(a, b):
    cociente_entero = a // b
    cociente_decimal = round(a / b, 3)
    return (cociente_entero, cociente_decimal)

opcion = input("Ingrese la opción deseada: ")

if opcion == "1":
    # Suma
    # Solicitar dos números al usuario y llamar a la función suma
    # Agregar el resultado parcial a la lista resultados
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    resultado = suma(num1, num2)
    resultados.append(resultado)
    print("Resultado: ", resultado)
elif opcion == "2":
    # Resta
    # Solicitar dos números al usuario y llamar a la función resta
    # Agregar el resultado parcial a la lista resultados
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    resultado = resta(num1, num2)
    print("Resultado:", resultado)
    seguir_operando = input("Desea seguir operando")
    while  seguir_operando == "yes":
        num = float(input("Ingrese el primer número: "))
        resultado = resta(num, resultado)
        break
    resultados.append(resultado)
    print("Resultado:", resultado)
elif opcion == "3":
    # Multiplicación
    # Solicitar dos números al usuario y llamar a la función multiplicacion
    # Agregar el resultado parcial a la lista resultados
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    resultado = multiplicacion(num1, num2)
    resultados.append(resultado)
    print("Resultado: ", resultado)
elif opcion == "4":
    # División
    # Solicitar dos números al usuario y llamar a la función division
    # Agregar el resultado parcial a la lista resultados
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    resultado = division(num1, num2)
    resultados.append(resultado)
    print("Resultado parcial:")
    print("Cociente entero:", resultado[0])
    print("Cociente decimal:", resultado[1])
else:
    print("Opción inválida")


    print("Resultados parciales:")
    for resultado in resultados:
        print(resultado)

    resultado_final = sum(numeros)
    print("Resultado final:", resultado_final)