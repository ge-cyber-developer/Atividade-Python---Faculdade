'''
4. Uma empresa paga seus vendedores com base em comissões. O vendedor recebe R\\$ 200 por semana mais 9 por cento de suas vendas brutas daquela semana. Por exemplo, um vendedor que teve vendas brutas de R\\$ 3000 em uma semana recebe R\\$ 200 mais 9 por cento de R\\$ 3000, ou seja, um total de R\\$ 470. Escreva um programa (usando listaa) que determine quantos vendedores receberam salários nos seguintes intervalos de valores:\n",
        "*  R\\$ 200 - R\\$ 299\n",
        "*  R\\$ 300 - R\\$ 399\n",
        "*  R\\$ 400 - R\\$ 499\n",
        "*  R\\$ 500 - R\\$ 599\n",
        "*  R\\$ 600 - R\\$ 699\n",
        "*  R\\$ 700 - R\\$ 799\n",
        "*  R\\$ 800 - R\\$ 899\n",
        "*  R\\$ 900 - R\\$ 999\n",
        "*  R\\$ 1000 em diante\n",
        "\n",
        "__Desafio__: Crie uma fórmula para chegar na posição da lista a partir do salário, sem fazer vários ``ifs`` aninhados."
'''

salarioBase = 200
vendedores = [0, 0, 0, 0, 0, 0, 0, 0, 0]
 
for i in range (0, 10):
 
    valorVendas = float(input("\nInforme o valor das vendas(semana): "))
    salario = valorVendas * 0.09 + salarioBase

    indice = int(salario/100) - 1

    if(indice > 9):
      indice = 9
 
    elif(indice < 1):
      indice = 1

    vendedores[indice - 1] += 1

    for i in range(0, 9):
      de = i*100 + 200  
      para = (i + 1) * 100 + 199
      print("R$", de, "- R$", para, " = ", vendedores[i], "Vendedor(es)")