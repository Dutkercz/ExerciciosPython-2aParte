from random import randint
from time import sleep

print('VAMOS JOGAR PAR OU IMPAR')
computador = randint(0,10)
soma = 0
contador = 0
escolha = ' '

while True:
    escolha = str(input('''Você quer: 
[P] - PAR 
[I] - IMPAR
>>>> ''')).strip().upper()[0]

    jogador = int(input('Escolha um numero de 0 a 10: '))
    print()
    if jogador < 11:
        soma = jogador + computador
        if soma % 2 == 0 and escolha == 'P':
            print('===' * 20)
            print('Você escolheu PAR')
            sleep(1)
            print(f' \033[32mVocê jogou {jogador}\033[m e o \033[31mPC {computador}\033[m, \033[34mTOTAL {soma}\033[m.')
            print(f'{soma} é PAR, \033[32mJOGADOR VENCE!\033[m ')
            sleep(1)
            contador += 1
            print('===' * 20)
        elif soma % 2 == 1 and escolha == 'I':
            print('===' * 20)
            print('Você escolheu IMPAR')
            sleep(1)
            print(f' \033[32mVocê jogou {jogador}\033[m e o \033[31mPC {computador}\033[m, \033[34mTOTAL {soma}\033[m.')
            print(f'{soma} é IMPAR, \033[32mJOGADOR VENCE!\033[m ')
            sleep(1)
            contador += 1
            print('===' * 20)
        elif soma % 2 == 0 and escolha == 'I':
            print('===' * 20)
            print('Você escolheu IMPAR')
            sleep(1)
            print(f' \033[32mVocê jogou {jogador}\033[m e o \033[31mPC {computador}\033[m, \033[34mTOTAL {soma}\033[m.')
            print(f'{soma} é PAR, \033[31mPC VENCE!\033[m ')
            print('===' * 20)
            sleep(1)
            break
        elif soma % 2 == 1 and escolha == 'P' :
            print('==='*20)
            print('Você escolheu PAR')
            sleep(1)
            print(f' \033[32mVocê jogou {jogador}\033[m e o \033[31mPC {computador}\033[m, \033[34mTOTAL {soma}\033[m.')
            print(f'{soma} é IMPAR, \033[31mPC VENCE!\033[m ')
            print('==='*20)
            sleep(1)
            break
    else:
        print('\033[31m==\033[m' * 20)
        print(f'\033[31m{'OPÇÃO INVÁLIDA!':=^40}\033[m')
        print('\033[31m==\033[m' * 20)

print(f'\033[31m{'GAME OVER':=^40}\033[m')
print(f'\033[33mTOTAL DE VITÓRIAS CONSECUTIVAS:\033[m \033[32m== {contador} ==\033[m')
