print('Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome')
nome=str(input('Digite seu nome: ')).title().strip()
print('Seu nome é {}'.format(nome))
print('Seu nome tem Silva?..... {}'.format('Silva'in nome))
