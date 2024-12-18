import math
from math import radians

print('Faça um prog. que leia um ângulo qualquer e mostre na tela o valor do:\nseno do cosseno e da tangente desse âgulo.')
angulo=int(input('Digite o valor de um ângulo: '))
rad= math.radians(angulo)
cos= math.cos(rad)
sen= math.sin(rad)
tang = math.tan(rad)
print('O valor de:\nSENO {:.2f}\nCOSSENO {:.2f}\nTANGENTE {:.2f}'.format(sen, cos,tang))