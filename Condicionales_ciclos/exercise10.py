"5. Escribir un programa que permita al usuario ingresar 6 números enteros, que pueden ser positivos o negativos. Al finalizar, mostrar la sumatoria de los números negativos y el promedio de los positivos."
try:
    # Inicializamos variables a se utilizadas
    suma = 0
    sum_negativos = 0
    prom = 0
    cantidad_positivos = 0
    # Establecemos el numero de elementos a ser capturado
    for i in range(6):
        # Capturamos los elementos
        num = int(input("Ingrese un número: "))
        # Verificamos si el elemento es positivo
        if num > 0:
            # Si es positivo generamos el promedio 
            cantidad_positivos +=1
            suma += num 
            prom = int(suma / cantidad_positivos)
        # Descartamos los negativos al no cumplir la primerac condicion
        else:
            # Si es negativo, sumamos al sumatorio de negativos
            sum_negativos += num
    # Establemos en mensaje para las verificaciones y sus resltados
    mensaje =f"El promedio de los positivos ingresados es: { prom }, y la sumatoria de los negativos: { sum_negativos }"
    # Mostramos el mensaje
    print(mensaje)
    # Manejo de errores en caso de que se ingrese caracteres erroneos
except ValueError:
    print("Error")