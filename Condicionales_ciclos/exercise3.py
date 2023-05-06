"#3 para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales o superiores a $1.000.000 mensuales. Escribir un programa que pregunte a usuario añ edad y sus ingresos  menusales y muyestre `pr àmtañña so eñ usuaro toeme que tributar o no"
import time
try:
    # Solicita al usuario ingresar su edad e ingresos
    edad = int(input("Digite su edad: "))
    ingreso = int(input("Digite su edad: "))
    # Verifica si el usuario tributa
    tributa = ("Usted no debe tributar")
    if edad > 16 and ingreso > 1000000:
        tributa = ("Udted debe tributar")
    # Muestra por pantalla la respuesta de la vericacion
    print(tributa)
# Manejo de errores en caso de que se ingrese caracteres erroneos
except ValueError:
    print("Error")