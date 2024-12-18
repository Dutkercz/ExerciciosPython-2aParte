from random import randint

pc = randint(0,10)
acertou = False
cont = 0
while acertou == False :
    jogador = int(input('escolha um número entre 0 e 10: '))
    cont += 1
    if jogador == pc:
        acertou = True
    else:
        if jogador < pc:
            print('Ta quente, MAIS ALTO!')
        elif jogador > pc:
            print('Ta quente... MAIS BAIXO!')
print('Você acertou com {} tentativas!'.format(cont))