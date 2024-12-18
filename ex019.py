
import random


print('Um professor quer sortear UM de seus QUATRO alunos para apagar o quadro\nFaça um programa para ajud-lo, lendo os seus nome e esolhendo um deles')
al1=str(input('Diga o nome do 1o aluno: '))
al2=str(input('Diga o nome do 2o aluno: '))
al3=str(input('Diga o nome do 3o aluno: '))
al4=str(input('Diga o nome do 4o aluno: '))
lista  = [al1,al2,al3,al4]
escolhido = random.choice(lista)
print('O aluno escolhido foi : {}'.format(escolhido))

