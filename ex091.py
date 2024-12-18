'''4 jogadores, jogam um dado...'''
from operator import itemgetter
from random import randint
from time import sleep

jogadores = {}
jogadores['jogador1']=randint(1,6)
jogadores['jogador2']=randint(1,6)
jogadores['jogador3']=randint(1,6)
jogadores['jogador4']=randint(1,6)
#print(sorted(jogadores.values(), reverse=True))
rank = {}

for key, val_k in jogadores.items():
    print(f' O {key}, tirou {val_k}')
    sleep(1)
rank = sorted(jogadores.items(), key=itemgetter(1), reverse = True) #itemgetter(1) quero sortear pelo valor 1 (0,1,2..)
print(rank)
print(f'{"RANK":=^32}')
for i, v in enumerate(rank):#no indice (i) de rank eu quero o valor(v) (usamos enumarate pois o itemgetter transforma-
    print(f'{i+1}° Lugar: {v[0]} com o numero {v[1]}')#nossas informações em uma LISTA COM TUPLAS