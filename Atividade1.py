'''1. Faça um Programa que leia 20 números inteiros e armazene-os em uma lista.
Armazene os números pares na lista PAR e os números IMPARES na lista ímpar. Imprima as três listas." '''

numero = 0

lista_numeros = []
lista_numeros_impares = []
lista_numeros_pares = []

for numero in range (1,20):
    lista_numeros.append(int(input("Digite um número: ")))

    for numero in range (1,20):
        if lista_numeros[numero] % 2 == 0:
            lista_numeros_pares.append(lista_numeros[numero])
        else :
            lista_numeros_impares.append(lista_numeros[numero])

print("lista com 20 números: " + str(lista_numeros))
print("lista com números pares: " + str(lista_numeros_pares))
print("lista com números impares: " + str(lista_numeros_impares))
