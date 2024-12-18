from time import sleep

vel=int(input('Digite a velocidade em que passou o carro Km/h: '))
multa=(vel-80)*7
acima= vel-80

if vel>80:
    print('Você passou a {} Km/h, isso é {} km/h acima do permitido de 80 Km/h'.format(vel,acima))
    sleep(3)
    print('E por isso recebeu uma multa de R$ {}'.format(multa))
else:
    print('Tenha um bom dia e continue a sua viagem com segurança!')
