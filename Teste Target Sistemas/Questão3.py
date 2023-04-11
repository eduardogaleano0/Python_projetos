# Questão 3
# a) 1, 3, 5, 7, ___
sequencia_a = [1, 3, 5, 7]
proximo_item_a = sequencia_a[-1] + 2
sequencia_a.append(proximo_item_a)
print(sequencia_a)

# b) 2, 4, 8, 16, 32, 64, ____
sequencia_b = [2, 4, 8, 16, 32, 64]
proximo_item_b = sequencia_b[-1] * 2
sequencia_b.append(proximo_item_b)
print(sequencia_b)

# c) 0, 1, 4, 9, 16, 25, 36, ____
sequencia_c = [0, 1, 4, 9, 16, 25, 36]
proximo_item_c = (len(sequencia_c))**2
sequencia_c.append(proximo_item_c)
print(sequencia_c)

# d) 4, 16, 36, 64, ____
sequencia_d = [4, 16, 36, 64]
proximo_item_d = sequencia_d[-1] + 20
sequencia_d.append(proximo_item_d)
print(sequencia_d)

# e) 1, 1, 2, 3, 5, 8, ____
sequencia_e = [1, 1, 2, 3, 5, 8]
proximo_item_e = sequencia_e[-1] + sequencia_e[-2]
sequencia_e.append(proximo_item_e)
print(sequencia_e)

# f) 2,10, 12, 16, 17, 18, 19, ____
sequencia_f = [2, 10, 12, 16, 17, 18, 19]
proximo_item_f = sequencia_f[-1] + 1
sequencia_f.append(proximo_item_f)
print(sequencia_f)
