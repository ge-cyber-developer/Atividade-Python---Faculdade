''' 3. Faça um programa que leia um número indeterminado de valores, correspondentes a notas, 
encerrando a entrada de dados quando for informado um valor igual a -1 (que não deve ser armazenado). 
Após esta entrada de dados, faça:\n",
        "\n",
        "*  Mostre a quantidade de valores que foram lidos;\n",
        "*  Exiba todos os valores na ordem em que foram informados, um ao lado do outro;\n",
        "*  Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;\n",
        "*  Calcule e mostre a soma dos valores;\n",
        "*  Calcule e mostre a média dos valores;\n",
        "*  Calcule e mostre a quantidade de valores acima da média calculada;\n",
        "*  Calcule e mostre a quantidade de valores abaixo de sete;\n",
        "*  Encerre o programa com uma mensagem;" '''

numeros = []
j = 0
i = 0
maiormedia = 0
menorsete = 0


while i != -1:
  numeros.append(int(input('Digite um número: ')))
  i=numeros[j]
  j = j+1

numeros.pop(j-1)
media = int(sum(numeros)/len(numeros))

print('\nNúmero total de números inseridos: '+str(len(numeros)))
print('Os números digitados foram:',str(numeros))
print('Números em ordem inversa um abaixo do outro:')

numeros.reverse()

for var in numeros:
  print('\tIndex('+str(numeros.index(var))+') = '+str(var))
  if(var>media):
    maiormedia = maiormedia + 1
  elif(var<7):
    menorsete = menorsete + 1

print('O valor da soma de todos os valores é: '+str(sum(numeros)))
print('A média dos valores é: '+str(media))
print('Quantidade de números acima da média: '+str(maiormedia))
print('Quantidade de números menores que 7: '+str(menorsete))
print('\nFim das informações, obrigado :)'