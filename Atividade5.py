'''
5. Foram anotadas as idades e alturas de 30 alunos. 
Faça um Programa que determine quantos alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos."
'''


alunos = []
media = 0
qtd = 0

for i in range(2): 
    idade = float(input("Idade: "))
    altura = float(input("Altura: "))
    alunos.append([idade, altura])

for j in range(len(alunos)): media += alunos[i][1]
media = media / len(alunos)

for l in range(len(alunos)):
    if alunos[i][0] > 13 and alunos[i][1] < media: ++qtd;

print("Quantidade de alunos com mais de 13 e altura inferior a media: ", qtd)