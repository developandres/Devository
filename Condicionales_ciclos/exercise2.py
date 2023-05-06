"#2 Solicitar al usuario que ingrese dos numeros y mostrar cual de los dos es menor"
try:
    # Solicita al usuario ingresar dos números enteros
    num = int(input("Ingrese un numero: "))
    num2 = int(input("Ingrese un numero: "))
    # Verifica cual de los numeros ingresados es el menor
    menor = "El menor es el primer numero",num
    if num > num2:
        menor="El menor es el segundo numero",num2
    # Muestra por pantalla el menor de los numeros ingresados
    print(menor)
    # Manejo de errores en caso de que se ingrese caracteres erroneos
except ValueError:
    print("Error")