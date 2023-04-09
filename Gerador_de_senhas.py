#Olá e bem-vindo ao projeto de gerador de senhas em Python! Este é um pequeno projeto que permite gerar senhas aleatórias usando o módulo random do Python. 
# A ideia é permitir que você possa gerar senhas fortes e seguras com facilidade e rapidez. O programa é simples de usar. Basta fornecer a quantidade de senhas que deseja gerar e o comprimento de cada uma delas. 
# O programa irá gerar senhas aleatórias compostas por letras maiúsculas e minúsculas, números e caracteres especiais.

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
for pwd in range(numeros) :
    password = ''
    for c in range(tamanho):
        password += random.choice(caracteres)
    print(password)

    