def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Error: División por cero."
    return a / b

def calcular(entrada):
    # Borramos espacios
    entrada = entrada.replace(" ", "")

    if entrada.lower() == "c":
        return "Operación borrada"

    for operador in ["+", "-", "", "/"]:
        if operador in entrada:
            # Separamos las partes del string
            partes = entrada.split(operador) 
            if len(partes) == 2:
                try:
                    a = float(partes[0])
                    b = float(partes[1])
                except ValueError:
                    return "Error: Entrada inválida."

                if operador == '+':
                    return sumar(a, b)
                elif operador == '-':
                    return restar(a, b)
                elif operador == '':
                    return multiplicar(a, b)
                elif operador == '/':
                    return dividir(a, b)

    return "Error: Operación no reconocida."

def main():
    while True:
        entrada = input("Ingrese una operación (o 'c' para borrar, 'q' para salir): ")
        if entrada.lower() == 'q':
            print("¡Gracias por usar la calculadora!")
            break
        resultado = calcular(entrada)
        print(f"Resultado: {resultado}")

if name == "main":
    main()