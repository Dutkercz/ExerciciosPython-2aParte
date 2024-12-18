soma = cont = 0
lista = []
while True:
    n = int(input('Digite um numero: '))
    continuar = str(input('Deseja continuar, [S]/[N]: ')).strip().lower()[0]
    soma += n
    cont += 1
    lista += [n]
    if continuar == 'n':
        break
print(lista)
media = soma/cont
maxvalor = max(lista)
minvalor = min(lista)
print(f'A soma dos {cont} numeros é {soma}')
print(f'A média é {media:.2f}, o maior numero é {maxvalor}, e o menor é {minvalor}')
