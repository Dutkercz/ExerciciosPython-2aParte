import random
from time import sleep
'''Pode-se usar ao inves de list "lis=[0,1,2,3,4,5]" um RANDINT(0, 5)'''
print('-=-' *20)
print('                  Jogo da Adivinhação')
print('-=-' *20)
sleep(0.5)
print('Estou pensando em um numero de 0 a 5...Você consegue adivinhar?!')
lis=[0,1,2,3,4,5]
esco=(random.choice(lis))

#print(esco)
sleep(2)
num=int(input('Digite um número e tente a sorte: '))
print('QUE RUFEM OS TAMBORES!!!!!!!!')
sleep(1)
print('...........')
sleep(1)
print('....')
sleep(3)
if num==esco:
    print('Nossa, você acertou em cheio, eu realmente estava pensando no número {}'.format(esco))
else:
    print('Hmmm...que pena, não foi dessa vez! Eu estava pensando no número {}'.format(esco))




