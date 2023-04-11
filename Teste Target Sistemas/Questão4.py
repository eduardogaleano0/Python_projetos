# Questão 4
# Distância entre Ribeirão Preto e Franca (em km)
distancia = 100

# Velocidade do carro e do caminhão (em km/h)
velocidade_carro = 110
velocidade_caminhao = 80

# Tempo que o caminhão leva a mais nos pedágios (em horas)
tempo_pedagio = 0.0833  

# Tempo que o carro e o caminhão levam para se cruzar (em horas)
tempo_cruzamento = distancia / (velocidade_carro + velocidade_caminhao)

# Distância percorrida pelo carro e pelo caminhão até o cruzamento (em km)
distancia_carro = velocidade_carro * tempo_cruzamento
distancia_caminhao = velocidade_caminhao * tempo_cruzamento

# Tempo que o caminhão leva a mais para passar pelos pedágios (em horas)
tempo_pedagio_caminhao = tempo_pedagio * 2 

# Distância percorrida pelo caminhão durante o tempo nos pedágios (em km)
distancia_pedagio_caminhao = velocidade_caminhao * tempo_pedagio_caminhao

# Distância total percorrida pelo caminhão (em km)
distancia_total_caminhao = distancia_caminhao + distancia_pedagio_caminhao

# Se o caminhão está mais próximo de Ribeirão Preto do que o carro
if distancia_total_caminhao < distancia_carro:
    print("O caminhão está mais próximo de Ribeirão Preto.")
else:
    print("O carro está mais próximo de Ribeirão Preto.")


"""As primeiras linhas do código definem as variáveis necessárias para o cálculo, como a distância entre as cidades, as velocidades do carro e do caminhão e o tempo que o caminhão leva a mais para passar pelos pedágios.
Em seguida, é calculado o tempo que o carro e o caminhão levam para se cruzar na rodovia, considerando as suas velocidades.
Com o tempo de cruzamento, é possível calcular a distância percorrida pelo carro e pelo caminhão até o ponto de encontro.
Depois, é calculado o tempo adicional que o caminhão leva para passar pelos pedágios e a distância que ele percorre durante esse tempo.
Por fim, é calculada a distância total percorrida pelo caminhão (incluindo os pedágios) e comparada com a distância percorrida pelo carro. Se a distância do caminhão for menor, isso significa que ele está mais próximo de Ribeirão Preto. Caso contrário, o carro está mais próximo."""
