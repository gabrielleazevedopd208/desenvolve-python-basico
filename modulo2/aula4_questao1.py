#Faça um programa para ler as dimensões de um terreno em inteiros (comprimento e largura), bem como o preço do metro quadrado da região em ponto flutuante. Calcule o valor do terreno e imprima o resultado como mostra o exemplo a seguir:
#O terreno possui 250m2 e custa R$512,490.50

# Lê a largura do terreno como número inteiro
largura = int(input("Digite a largura: "))

# Lê o comprimento do terreno como número inteiro
comprimento = int(input("Digite o comprimento: "))

# Lê o preço do metro quadrado da região como número decimal (ponto flutuante)
preco_m2 = float(input("Digite o preço do m² na região: "))

# Calcula a área do terreno em metros quadrados
area_m2 = comprimento * largura

# Calcula o valor total do terreno
preco_total = preco_m2 * area_m2

# Exibe a área e o valor total do terreno formatado com duas casas decimais
print(f"O terreno possui {area_m2}m² e custa R${preco_total:,.2f}")

