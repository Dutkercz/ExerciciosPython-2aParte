from random import randint
print('Jogo da adivinhação!')
pcesco= randint(0,10)

cont = 1
jogador = int(input('''Estou pensando em número entre 0 e 10. Consegue adivinhar?
 DIGITE:> '''))
while pcesco != jogador:
    cont += 1
    if pcesco > jogador:
        jogador = int(input('Hmm...errou, \033[34mMAIS!\033[m tente novamente: '))
    elif pcesco < jogador:
        jogador = int(input('Hmm...errou, \033[31mMENOS!\033[m tente novamente: '))
print('Você \033[32mACERTOU\033[m, eu escolhi o n° {}, você levou {} tentativas para acertar!'.format(pcesco, cont))