'''ANALISADOR DE SEXO M OU F'''

sexo = str(input('''Digite seu sexo:
M - masculino
F - feminino
:>''')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Digite um opção válida: M ou F: ')).strip().upper()[0]
print('Você se registrou como {}'.format(sexo))