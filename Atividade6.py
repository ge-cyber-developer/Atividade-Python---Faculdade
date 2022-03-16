'''
6. Faça um Programa que leia uma lista A com 10 números inteiros, calcule e mostre a soma dos quadrados dos elementos contidos na lista."
'''

numeros = []
quadrado = []
soma = 0

for i in range(3):
  numeros.append(int(input("Digite um número: ")))
  quadrado.insert(i,numeros[i]*numeros[i])
  soma = soma+quadrado[i]
print('A soma dos quadrados de todos os itens é',soma)