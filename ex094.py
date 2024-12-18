candidatos = list()
person = {}
contador = media = 0
contM = []
acimaM = []
while True:
    person['Nome'] = str(input('Nome: ')).strip().title()
    person['Sexo'] = str(input('Sexo M / F : ')).strip().upper()[0]
    person['Idade'] = int(input('Idade: '))

    cont = str(input('Deseja continuar a cadastrar? [S]/ [N]: ')).strip().lower()[0]
    if person['Idade'] > 0:
        candidatos.append(person.copy())
        contador += 1
        media += person['Idade']
        if person['Sexo']=='F':
            contM.append(person['Nome'])
        print(f'\033[32mCADASTRO DE {person["Nome"]} concluido!\033[m')
    elif person['Idade'] <= 0:
        print('\033[31mINFORMAÇÕES INVALIDAS\033[m')
    if cont == 'n':
        break

media = media/len(candidatos)

print('*=*'*20)
print(f'Ao todos temos {contador} pessoas cadastradas!')
print(f'A média de idade é de {media:.2f}.')
print(f'As mulheres cadastradas foram: ', end='')
for c in contM:
    print(f'{c}', end=' ,')
print('...fim da lista.')
print('Os candidatos acima da média são: ')
for c in candidatos:
    if c['Idade'] > media:
        print('  ', end=' ')
        for k , valk in c.items():
            print(f'{k } : {valk}', end=' > ')
        print()
