#Escreva um programa que leia um valor inteiro referente a uma quantia em reais e calcule a menor quantidade possível de notas necessárias para pagar aquele valor. As notas possíveis são: 100, 50, 20, 10, 5, 2, 1. A saída deve estar formatada exatamente como indicado.

v = int(input("Digite um valor em RS:"))
a = v//100
v = v % 100

b = v//50
v = v % 50

c = v//20
v = v % 20

d = v//5
v = v % 5

e = v//2
v = v % 2

f = v//1
v = v % 1

print(f"{a} nota(s) de R$ 100,00")
print(f"{b} nota(s) de R$ 50,00")
print(f"{c} nota(s) de R$ 20,00")
print(f"{d} nota(s) de R$ 10,00")
print(f"{e} nota(s) de R$ 5,00")
print(f"{f} nota(s) de R$ 2,00")
