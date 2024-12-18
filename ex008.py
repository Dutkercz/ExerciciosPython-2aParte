from logging.config import dictConfig

print('Calcule a distancia em todas a medidas de distância')
medida=float(input('Distancia em metros:'))
dm = medida *10
cm = medida * 100
mm = medida * 1000
dc = medida /10
hc = medida /100
km = medida /1000
print('A distancia em dm é: {}dm\nEm cm é {}cm\nE a ditância em mm é {}mm' .format (dm, cm, mm))
print('E a distancia em {}dc\nEm hc é {}hc\nE em km é {}km'.format(dc, hc, km))
