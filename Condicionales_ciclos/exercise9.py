"4. hacer un programa qyeu solicite 10 edades y luego calcule el promedie edad de aquellas personas mayores a 18 años"
try:
    # Inicializamos variables a se utilizadas
    suma = 0
    cont = 0
    # Generamos la cantidad de edades a ser capturadas
    for i in range(10): 
        # Capturamos las edades
        num = int(input("Edad: "))
        # Verificamos cuantas de las edades ingresadas son mayores a 18
        if num > 18:
            # Generamos el promedio de los que cumplen la verificaion
            cont+=1
            suma += num
            # Calculamos el promedio
        prom = int(suma / cont)
        # Mostramos el promedio
    print(f"Promedio de edad: { prom }")
    # Manejo de errores en caso de que se ingrese caracteres erroneos
except ValueError:
    print("Error")