''' 2. Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma
lista. Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas 
_acima da média anual__, e em que mês elas ocorreram (mostrar o mês por extenso: 1-Janeiro, 2-Fevereiro, . . . )." '''



numero = 0

lista_numeros = []
lista_numeros_impares = []
lista_numeros_pares = []

for numero in range (1,20):
    lista_numeros.append(int(input("Digite um número: ")))
    if lista_numeros[numero] % 2 == 0:
        lista_numeros_pares.append(lista_numeros[numero])
    else :
        lista_numeros_impares.append(lista_numeros[numero])

print("lista com 20 números: " + str(lista_numeros))
print("lista com números pares: " + str(lista_numeros_pares))
print("lista com números impares: " + str(lista_numeros_impares))