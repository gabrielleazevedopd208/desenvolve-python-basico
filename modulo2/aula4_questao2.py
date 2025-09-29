#Leia um valor inteiro correspondente a uma temperatura em graus Fahrenheit e apresente-a convertida em graus Celsius. 
#Fórmula de conversão: C = (F - 32) * (5/9), sendo C o valor em graus Celsius e F o valor em Fahrenheit. Antes de imprimir, converta o valor em Celsius para inteiro. 

# Lê a temperatura em Fahrenheit como número inteiro
F = int(input("Digite a temperatura em Fahrenheit: "))
# Converte de Fahrenheit para Celsius usando a fórmula
C = int((F - 32) * (5 / 9)) 
# Exibe a mensagem 
print(f"{F} graus Fahrenheit são {C} graus Celsius.")

