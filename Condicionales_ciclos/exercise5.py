"5. En una determinada empresa sus empleados son evaluados al final de cada año. Los puntos que pueden obtener en la evaluación pueden ser 0.0, 0.4, 0.6 o más, pero no valores intermedios entre las cifras mencionadas. La cantidad de dinero conseguida en cada nivel es de $35.000 multiplicada por la puntuación del nivel. Escribir un programa que lea la puntuación del usuario e indique su nivel de rendimiento, así como la cantidad de dinero que recibirá el usuario."
try:
    # Solicita al usuario ingresar su rendimiento
    rendimiento = float(input("Ingrese su rendimiento: "))
    # Verifica el puntaje y el rendimiento
    puntaje = "Excelente"
    remuneracion = int(35000 * 0.6)
    if rendimiento == 0.0:
        puntaje = "Insuficiente"
        remuneracion = int(35000 * 0.0)
    elif rendimiento == 0.4:
        puntaje = "Aceptable"
        remuneracion = int(35000 * 0.4)
    # Almacena el mensaje con los datos de la verificacion
    mensaje = f"Su respectivo puntaje { puntaje } y su respectiva remuneracion segun su puntaje es { remuneracion }"
    # Muestra por pantalla el mensaje que contiene la verificaion
    print(mensaje)
    # Manejo de errores en caso de que se ingrese caracteres erroneos
except ValueError:
    print("Puntuacion ingresada erronea")