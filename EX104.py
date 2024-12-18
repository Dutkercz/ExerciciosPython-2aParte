#ROTINAS
from unicodedata import numeric


def leiaInt(msg):
    value = None
    while True:
        numero = input(f'{msg}')
        if  numero.isnumeric():
            value = numero
            return numero
            break
        else:
            print('\033[31mERRO! Digite um numero válido.\033[m')


n = leiaInt('Digite um numero: ')
print(f'Você digitou o número {n}')