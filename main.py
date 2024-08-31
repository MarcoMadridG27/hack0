def sumar(a,b):
    return a + b
    

def calcular(entrada):
    #Borramos espacios
    entrada = entrada.replace(" ","")
    
    if entrada.lower("c"):
        return "Operación borrada"
    
    for operador in ["+"]:
        if operador in entrada:
            #Separamos las partes del string
            partes = entrada.split(operador) 
            if len(partes) == 2:
                try:
                    a = float(partes[0])
                    b = float(partes[1])    
                except ValueError:
                    return "Error: Entrada inválida."
                #Suma
                if operador == '+':
                    return sumar(a, b)
                
while True:
    entrada = input("Ingrese una operación (o 'c' para borrar): ")
    resultado = calcular(entrada)
    print(f"Resultado: {resultado}")