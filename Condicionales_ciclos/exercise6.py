"6. Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad)."
try:
    # Solicita al usuario ingresar su edad
    edad = int(input("Ingrese su edad:"))
    # Genera una lista con numeros desde 1 hasta la edad ingresada
    for i in range(1,edad+1):
    # Muestra por pantalla la lista de numeros 
        print(i)
    # Manejo de errores en caso de que se ingrese caracteres erroneos
except ValueError:
    print("Edad incorrecta")
