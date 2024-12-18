'''Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
No final do programa, mostre:
a média de idade do grupo,
qual é o nome do homem mais velho e
quantas mulheres têm menos de 20 anos.'''

idadeM = 0
cont = 0
maisvelhoI = 0
maisvelhoN = ''
for c in range (1,5):
    nome = str(input('Digite o nome da {}° pessoa: '.format(c)))
    idade = int(input('Digite a idade da {}° pessoa: '.format(c)))
    sexo = str(input('''Digite
    M - para masculino
    F - para feminino
    > ''')).strip().lower()
    idadeM += idade
    idadeM = idadeM/c
    if sexo == 'm' and idade > maisvelhoI:
        maisvelhoI = idade
        maisvelhoN = nome
    if sexo == 'f' and idade < 20:
        cont += 1
print('O homem mais velho é {} com {} anos.'.format(maisvelhoN.title() , maisvelhoI))
print('A média de idade do grupo é {:.2f}'.format(idadeM))
print('O grupo tem {} mulheres com menos de 20 anos.'.format(cont))