# Entrar via teclado com o valor da cotação do dólar e uma certa quantidade de dólares. Calcular e exibir o valor correspondente em Reais (R$).

# Solicita entrada de dados para o usuário e grava o valor digitado em uma variável "a"
c = float(input('Digite a cotação do dólar em R$: '))

# Solicita entrada de dados para o usuário e grava o valor digitado em uma variável "b"
d = float(input('Digite a quantia em dólar: '))

# Solicita entrada de dados para o usuário e grava o valor digitado em uma variável "c"
r = c * d

# Exibe a cotação do real é
print(f'O valor convertido é R$ {r:.2f} baseado na cotação {c:.2f}')