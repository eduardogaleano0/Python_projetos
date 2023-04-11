# Questão 2
def fibonacci(numero):
    #Calcula a sequência de Fibonacci até o número informado e verifica se ele pertence à sequência de Fibonacci
    a, b = 0, 1
    while a <= numero:
        if a == numero:
            return f"O número {numero} pertence à sequência de Fibonacci."
        a, b = b, a + b
    return f"O número {numero} não pertence à sequência de Fibonacci."

numero = int(input("Digite um número para verificar se ele pertence à sequência de Fibonacci: "))
print(fibonacci(numero))