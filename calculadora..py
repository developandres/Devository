class Calculadora:
    def __init__(self):
        pass
    
    def suma (self):
        num_digitos = int(input("Ingrese la cantidad de números a operar: "))
        num1 = int(input("Ingrese el primer número: "))
        num2 = int(input("Ingrese el segundo número: "))
        resultado_parcial = num1 + num2
        print("El resultado parcial de la operación es:", resultado_parcial)
        for i in range(num_digitos - 2):
            num = int(input("Ingrese otro número: "))
            resultado_total = resultado_parcial + num
            print("El resultado total de la operación es:", resultado_total)
            num1 = resultado_parcial
            num2 = num1 + num2
            resultado_parcial = resultado_total
        opcion = input("¿Desea seguir operando? (S/N): ")
        while opcion == "si":
            num_adicional = int(input("Ingrese otro número: "))
            resultado_total += num_adicional
            print("El resultado total de la operación es:", resultado_total)
            opcion = input("¿Desea seguir operando? (S/N): ")
        if opcion != "si":
            return None
    def resta (self):
        num_digitos = int(input("Ingrese la cantidad de números a operar: "))
        num1 = int(input("Ingrese el primer número: "))
        num2 = int(input("Ingrese el segundo número: "))
        resultado_parcial = num1 - num2
        print("El resultado parcial de la operación es:", resultado_parcial)
        for i in range(num_digitos - 2):
            num = int(input("Ingrese otro número: "))
            resultado_total = resultado_parcial - num
            print("El resultado total de la operación es:", resultado_total)
            num1 = resultado_parcial
            num2 = num1 - num2
            resultado_parcial = resultado_total
        opcion = input("¿Desea seguir operando? (S/N): ")
        while opcion == "si":
            num_adicional = int(input("Ingrese otro número: "))
            resultado_total -= num_adicional
            print("El resultado total de la operación es:", resultado_total)
            opcion = input("¿Desea seguir operando? (S/N): ")
        if opcion != "si":
            return None

    def multiplicacion (self):
        num_digitos = int(input("Ingrese la cantidad de números a operar: "))
        num1 = int(input("Ingrese el primer número: "))
        num2 = int(input("Ingrese el segundo número: "))
        resultado_parcial = num1 * num2
        print("El resultado parcial de la operación es:", resultado_parcial)
        for i in range(num_digitos - 2):
            num = int(input("Ingrese otro número: "))
            resultado_total = resultado_parcial * num
            print("El resultado total de la operación es:", resultado_total)
            num1 = resultado_parcial
            num2 = num1 * num2
            resultado_parcial = resultado_total
        opcion = input("¿Desea seguir operando? (S/N): ")
        while opcion == "si":
            num_adicional = int(input("Ingrese otro número: "))
            resultado_total *= num_adicional
            print("El resultado total de la operación es:", resultado_total)
            opcion = input("¿Desea seguir operando? (S/N): ")
        if opcion != "si":
            return None
    def division (self):
        num_digitos = int(input("Ingrese la cantidad de números a operar: "))
        num1 = int(input("Ingrese el primer número: "))
        num2 = int(input("Ingrese el segundo número: "))
        resultado_parcial = num1 / num2
        print("El resultado parcial de la operación es:", int(resultado_parcial))
        print("El resultado parcial de la operación es: {:.3f}".format(resultado_parcial))
        for i in range(num_digitos - 2):
            num = int(input("Ingrese otro número: "))
            resultado_total = resultado_parcial / num
            print("El resultado total de la operación es:", int(resultado_total))
            print("El resultado total de la operación es: {:.3f}".format(resultado_total))
            num1 = resultado_parcial
            num2 = num1 / num2
            resultado_parcial = resultado_total
        opcion = input("¿Desea seguir operando? (S/N): ")
        while opcion == "si":
            num_adicional = int(input("Ingrese otro número: "))
            resultado_total /= num_adicional
            print("El resultado total de la operación es:", int(resultado_total))
            print("El resultado total de la operación es: {:.3f}".format(resultado_total))
            opcion = input("¿Desea seguir operando? (S/N): ")
        if opcion != "si":
            return None
        
    def mostrar_menu(self):
        while True:
            print("Calculadora")
            print("")
            print("Ingrese + para sumar: ")
            print("Ingrese - para restar: ")
            print("Ingrese * para multiplicar: ")
            print("Ingrese / para dividir: ")
            print("0. Salir")
            print("")

            try:
                op = int(input("Digite la opcion: "))
                if op == 1:
                    self.suma()
                elif op == 2:
                    self.resta()
                elif op == 3:
                    self.multiplicacion()
                elif op == 4:
                    self.division()
                elif op == 0:
                    break
                else:
                    print("Opcion invalida")
            except ValueError:
                print("Error: opción inválida")

if __name__ == '__main__':
    calculadora = Calculadora()
    calculadora.mostrar_menu()