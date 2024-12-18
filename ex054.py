from datetime import date
print('Grupo da Maioridade')
cont1 = 0
cont2 = 0
anoA = date.today().year
for c in range (1,8):
    ano = int(input('Digite a data de nascimento do {}° candidato: '.format(c)))
    ano = anoA - ano
    if ano >= 18:
        cont1 += 1
    elif ano < 18:
        cont2 +=1
print('Nesse grupo de 7 pessoas, {} já são maiores de idade, e {} são menores!'.format(cont1,cont2))
