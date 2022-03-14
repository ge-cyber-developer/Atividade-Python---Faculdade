''' 2. Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma
lista. Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas 
_acima da média anual__, e em que mês elas ocorreram (mostrar o mês por extenso: 1-Janeiro, 2-Fevereiro, . . . )." '''



meses_do_ano = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
temperatura_media = []

for mes in range(0, len(meses_do_ano)):
    temperatura_media.append(float(input('Digite a temperatura média de ' + meses_do_ano[mes] + ':' )))
temperatura_media_anual = sum(temperatura_media)/len(temperatura_media)

for mes in range(0, len(temperatura_media)):
    if temperatura_media[mes] > temperatura_media_anual:
        print (str(mes+1) + " - " + meses_do_ano[mes])