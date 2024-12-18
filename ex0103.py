#ROTINAS
def ficha(n, g):
    print(f'O jogador {nome}, fez {gols} gol(s) no campeonato.')

#PROGRAMA PRINCIPAL
nome = str(input('Nome do jogador: '))
if len(nome) == 0:
    nome = '<Deconhecido>'
gols = str(input('Numero de gols do jogador: '))
if len(gols) == 0:
    gols = '0'
ficha(nome, gols)