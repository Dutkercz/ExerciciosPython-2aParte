from random import randint
from time import sleep

jogos = []
listaux = []

nj = int(input('Quantos jogos você quer fazer? '))
contJ = 0
while not  contJ == nj:
    cont = 0
    while True:
        num = randint(1,60)
        if num not in listaux:
            listaux.append(num)
            cont += 1
        if cont == 6:
            break
    contJ += 1
    jogos.append(listaux[:])
    listaux.clear()
print('\033[32mConsegui gerar o seguintes numeros para você:\033[m')
for c in range (0, len(jogos)):
    print(f'=='*20)
    print(f'Gerando o jogo {c+1}: {sorted(jogos[c])}')
    sleep(1)