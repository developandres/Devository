"3. hacer un programa que solicite 10 numeros y calcule y emita por pantalla cantos son positivos(mayores a cero)"
try:
    # Inicializamos variables a se utilizadas
    cont = 0
    # Generamos la cantidad de numeros a ser capturados
    for i in range(10):
        # Capturamos los numeros
        numeros = int(input("Numero: "))
        # Verificamos la cantidad de numeros positivos
        if numeros > 0:
            cont += 1
    # Mostramos por pantalla un mensaje con la cantidad de numeros
    print(f"La cantidad de positivos ingresados es: { cont }")
    # Manejo de errores en caso de que se ingrese caracteres erroneos
except ValueError:
    print("Error")