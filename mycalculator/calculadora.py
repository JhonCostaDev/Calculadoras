# Calculadora
# Pegar numeros 
# realizar operações (+, -, *, /)

def separa_expressao(expressao):
    numeros = ''
    operadores = []
    resultado = []

    for caractere in expressao:
        if caractere.isdigit():
            numeros += caractere
        else:
            resultado.append(numeros)
            numeros = ''
            resultado.append(caractere)
    if numeros:
        resultado.append(numeros)
    return resultado

def calcular(lista):
    # Separar numeros de operacao
    numeros = lista[::2]
    operacoes = lista[1::2]
    numeros = [float(item) for item in numeros]
    
    #identificar a operacao
    for operacao in operacoes:
        if operacao == "+":
            numeros[0] = numeros[0] + numeros[1]
            numeros.pop(1)
            
        if operacao == "-":
            numeros[0] = numeros[0] - numeros[1]
            numeros.pop(1)
            
        if operacao == "*":
            numeros[0] = numeros[0] * numeros[1]
            numeros.pop(1)
            
        if operacao == "/":
            numeros[0] = numeros[0] / numeros[1]
            numeros.pop(1)

    return numeros

user_input = input("Type your expression\n")
separado = separa_expressao(user_input)


resultado = calcular(separado)
print(resultado)