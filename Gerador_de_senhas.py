## Olá e bem-vindo ao projeto de gerador de senhas em Python!
## Este é um pequeno projeto que permite gerar senhas aleatórias usando o módulo random do Python.
## A ideia é permitir que você possa gerar senhas fortes e seguras com facilidade e rapidez.

# Importando a biblioteca Random, que será utilizada para gerar as senhas aleatórias
import random

# Mensagem de boas-vindas para o usuário.
print('Bem vindo ao gerador de senhas')

# Criando uma lista de caracteres que será utilizada para gerar as senhas
caracteres = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*().-_+,./ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# Pedindo para o usuário digitar a quantidade de senhas que deseja gerar
numeros = input('Quantidade de senhas para gerar: ')
numeros = int(numeros)

# Pedindo para o usuário digitar o tamanho da senha que deseja gerar
tamanho = input('Comprimento da senha: ')
tamanho = int(tamanho)

# Gerando as senhas
# Cria uma variável vazia para armazenar a senha gerada
for pwd in range(numeros) :
# Cria uma variável vazia para armazenar a senha gerada
    password = ''
# Loop que adiciona o tamanho de caracteres aleatórios à senha
    for c in range(tamanho):
# Adiciona um caractere aleatório à senha
        password += random.choice(caracteres)
# Imprime a senha gerada na tela
    print("A senha gerada é: ", password)