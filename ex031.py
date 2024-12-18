print('Vamos calcular o valor da sua passagem')
distancia=float(input('Qual a distâcia da sua viagem Km: '))
if distancia <=200:
    total1=distancia*0.50
    print('O total da passagem em uma viagem de {} Km é R$ {:.2f}'.format(distancia,total1))
else:
    total2=distancia*0.45
    print('O total da passagem em uma viajem de {} Km é R$ {:.2f}'.format(distancia,total2))