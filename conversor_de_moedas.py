# Importa as bibliotecas requests e json.
import requests
import json

# Faz uma requisição GET à API da AwesomeAPI que fornece a cotação do dólar, euro e libra esterlina em relação ao real brasileiro.
cotacoes = requests.get("https://economia.awesomeapi.com.br/all/USD-BRL,EUR-BRL,GBP-BRL")

# Converte a resposta em um dicionário.
cotacoes_dic = cotacoes.json()

# Extrai as cotações de cada moeda.
cotacao_dolar = float(cotacoes_dic["USD"]["bid"])
cotacao_euro = float(cotacoes_dic["EUR"]["bid"])
cotacao_libra = float(cotacoes_dic["GBP"]["bid"])

# Exibe as opções do menu e solicita que o usuário informe a opção desejada.
print("Menu:")
print("1 - Converter Dólar")
print("2 - Converter Euro")
print("3 - Converter Libra Esterlina")
print("4 - Sair")
opcao = int(input("Digite a opção desejada: "))

# Realiza a conversão de acordo com a opção escolhida.
if opcao == 1:
    # Solicita que o usuário informe uma quantidade em dólares, que é armazenada na variável d.
    d = float(input('Digite a quantia em dólar: '))
    # Calcula o valor correspondente em reais multiplicando a quantidade em dólares pela cotação do dólar, e armazena o resultado na variável r.
    r = cotacao_dolar * d
    # Imprime o valor convertido em reais, formatado com duas casas decimais, juntamente com a cotação do dólar utilizada no cálculo.
    print(f'O valor convertido é R$ {r:.2f} baseado na cotação {cotacao_dolar:.2f}')
elif opcao == 2:
    # Solicita que o usuário informe uma quantidade em euros, que é armazenada na variável e.
    e = float(input('Digite a quantia em euro: '))
    # Calcula o valor correspondente em reais multiplicando a quantidade em euros pela cotação do euro, e armazena o resultado na variável r.
    r = cotacao_euro * e
    # Imprime o valor convertido em reais, formatado com duas casas decimais, juntamente com a cotação do euro utilizada no cálculo.
    print(f'O valor convertido é R$ {r:.2f} baseado na cotação {cotacao_euro:.2f}')
elif opcao == 3:
    # Solicita que o usuário informe uma quantidade em libras esterlinas, que é armazenada na variável l.
    l = float(input('Digite a quantia em libra esterlina: '))
    # Calcula o valor correspondente em reais multiplicando a quantidade em libras esterlinas pela cotação da libra esterlina, e armazena o resultado na variável r.
    r = cotacao_libra * l
    # Imprime o valor convertido em reais, formatado com duas casas decimais, juntamente com a cotação da libra esterlina utilizada no c.
    print(f'O valor convertido é R$ {r:.2f} baseado na cotação {cotacao_libra:.2f}')
elif opcao == 4:
    print("Saindo...")