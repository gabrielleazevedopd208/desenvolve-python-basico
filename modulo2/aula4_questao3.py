#Você está desenvolvendo um programa para calcular o preço total de uma compra em uma loja online. O preço dos produtos é calculado multiplicando a quantidade pelo preço unitário. Escreva um programa em Python que solicite do usuário o nome, o preço unitário e a quantidade de 3 produtos comprados e imprima ao final o preço total da compra.

# produto 1
p1n = input("Digite o nome do produto 1: ")
p1p = float(input("Digite o preço unitário do produto 1: "))
p1q = int(input("Digite a quantidade do produto 1: "))

# produto 2
p2n = input("Digite o nome do produto 2: ")
p2p = float(input("Digite o preço unitário do produto 2: "))
p2q = int(input("Digite a quantidade do produto 2: "))

# produto 3
p3n = input("Digite o nome do produto 3: ")
p3p = float(input("Digite o preço unitário do produto 3: "))
p3q = int(input("Digite a quantidade do produto 3: "))

# cálculo do preço total da compra
s = (p1p * p1q) + (p2p * p2q) + (p3p * p3q)

# exibe o resultado formatado com 2 casas decimais
print(f"Total: R${s:,.2f}")
