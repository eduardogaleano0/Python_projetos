# Entrar via teclado com o valor de cinco produtos. Após as entradas, digitar um valor referente ao pagamento da somatória destes valores. Calcular e exibir o troco que deverá ser devolvido.

# Entrada dos valores dos produtos
produto1 = float(input("Digite o valor do primeiro produto: "))
produto2 = float(input("Digite o valor do segundo produto: "))
produto3 = float(input("Digite o valor do terceiro produto: "))
produto4 = float(input("Digite o valor do quarto produto: "))
produto5 = float(input("Digite o valor do quinto produto: "))

# Cálculo da soma dos valores dos produtos
total = produto1 + produto2 + produto3 + produto4 + produto5

# Entrada do valor do pagamento
pagamento = float(input("Digite o valor do pagamento: "))

# Cálculo do troco
troco = pagamento - total

# Exibição do troco
print(f"O troco a ser devolvido é de R${troco:.2f}")