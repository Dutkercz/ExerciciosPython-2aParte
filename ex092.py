from datetime import date
dados = {}
#1 coletando dados:
dados['Nome']=str(input('Nome: ')).strip().title()
#1.1 calculando idade
nas=int(input('Nascimento: '))
anoatual = date.today().year
dados['Idade']= anoatual - nas
dados['CTPS']=int(input('N° da CTPS: [0] - Não possui CTPS: '))
#1.2 Colentando dados, e calculo de possivel aposentadoria, com 35 anos trabalhados.
if dados['CTPS'] > 0:
    dados['Contratação'] = int(input('Ano de contratação: '))
    dados['Salario'] = int(input('Salário: '))
    dados['Aposentadoria'] = dados['Contratação']+35 - nas
else:
    dados['CTPS']='Não possui CTPS.'
for val , val_k in dados.items():
    print(f'{val} : {val_k}')