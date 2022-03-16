'''
7. Faça um Programa que leia uma lista de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes."
'''

chars = []
vogais = ['a', 'e', 'i', 'o', 'u']
charsConsoantes = []

for i in range(10):
    chars.append(input("Digite uma letra: "))

for i in range(len(chars)):
    for j in range(len(vogais)):
        if chars[i] == vogais[j]:
            charsConsoantes.append(chars[i])


print("Numero de consoantes: ", len(chars) - len(charsConsoantes))