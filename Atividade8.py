'''
8. Uma grande emissora de televisão quer fazer uma enquete entre os seus telespectadores para saber qual o melhor jogador após cada jogo. Para isto, faz-se necessário o desenvolvimento de um programa, que será utilizado pelas telefonistas, para a computação dos votos. Sua equipe foi contratada para desenvolver este programa.\n",
        "Para computar cada voto, a telefonista digitará um número, entre 1 e 23, correspondente ao número da camisa do jogador. Um número de jogador igual zero, indica que a votação foi encerrada. Se um número inválido for digitado, o programa deve ignorá-lo, mostrando uma breve mensagem de aviso, e voltando a pedir outro número. Após o final da votação, o programa deverá exibir:\n",
        "\n",
        "*  O total de votos computados;\n",
        "*  Os números e respectivos votos de todos os jogadores que receberam votos;\n",
        "*  O percentual de votos de cada um destes jogadores;\n",
        "*  O número do jogador escolhido como o melhor jogador da partida, juntamente com o número de votos e o percentual de votos dados a ele.\n",
        "\n",
        "A saída deverá ser algo semelhante ao exemplo abaixo:\n",
        "\n",
        "```\n",
        "Enquete: Quem foi o melhor jogador?\n",
        "\n",
        "Número do jogador (0=fim): 9\n",
        "Número do jogador (0=fim): 10\n",
        "Número do jogador (0=fim): 9\n",
        "Número do jogador (0=fim): 10\n",
        "Número do jogador (0=fim): 11\n",
        "Número do jogador (0=fim): 10\n",
        "Número do jogador (0=fim): 50\n",
        "Informe um valor entre 1 e 23 ou 0 para sair!\n",
        "Número do jogador (0=fim): 9\n",
        "Número do jogador (0=fim): 9\n",
        "Número do jogador (0=fim): 0\n",
        "\n",
        "Resultado da votação:\n",
        "\n",
        "Foram computados 8 votos.\n",
        "\n",
        "Jogador     Votos         %\n",
        "9               4     50,0%\n",
        "10              3     37,5%\n",
        "11              1     12,5%\n",
        "\n",
        "O melhor jogador foi o número 9, com 4 votos, correspondendo a 50% do total de votos.\n",
        "```"
'''
votosEmAtletas = [0] * 23
numeroAtleta = -1

ContadorVotos = 0
print('Enquete: Quem foi o melhor jogador?')

while (numeroAtleta != 0):
    numeroAtleta = int(input('Numero do jogador (0=fim): '))
    if (numeroAtleta < 0) or (numeroAtleta > 23):
        print('Informe um valor entre 1 e 23 ou 0 para sair!')
        continue
    if (numeroAtleta != 0):
        votosEmAtletas[numeroAtleta - 1] += 1
        ContadorVotos += 1

print('Resultado da votacao:')
print('Foram computados %d votos' % ContadorVotos)
print('Jogador\tVotos\t%%')

contador = 1
melhorJogador = 0

for votosAtleta in votosEmAtletas:
    if (votosAtleta > 0):
        print('%d\t%d\t%.2f%%' %\
              (contador, votosAtleta, votosAtleta / float(ContadorVotos) * 100))
        if (votosAtleta > votosEmAtletas[melhorJogador]):
            melhorJogador = contador - 1
    contador += 1

print('O melhor jogador foi o numero %d, com %d votos, correspondendo a '\
    '%.2f%% do total de votos' %\
    (melhorJogador + 1, votosEmAtletas[melhorJogador],
        votosEmAtletas[melhorJogador] / float(ContadorVotos) * 100))