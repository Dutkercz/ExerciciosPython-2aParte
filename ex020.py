import random

print('Defina a ordem de apresentação dos alunos')
a1=str(input('Primeiro aluno: '))
a2=str(input('Segundo aluno: '))
a3=str(input('Terceiro aluno: '))
a4=str(input('Quarto aluno: '))
lista=[a1, a2, a3, a4]
random.shuffle(lista)
print('A ordem de apresentação será: {}'.format (lista))

print('sorteando um numero')
n1=str(input('Diga o 1o nome: '))
n2=(str(input('Diga o 2o nome: ')))
n3=str(input('Diga o 3o nome: '))
n4=str(input('Diga o 4o nome: '))
lis=[n1,n2,n3,n4]
escolha=random.choice(lis)
print('O numero escohido é : ',escolha)
