lista = list()
numeros = list()
while True:
    valor=int(input('Digite os valores desejados: '))
    if valor not in lista:
        print('Valor ADICIONADO!')
        lista.append(valor)
    else:
        print('Valor Duplicado, VALOR DESCONSIDERADO!')

    cont = str(input('Deseja continuar [S/N]')).strip().lower()[0]
    if cont == 'n':
        break
lista.sort()
print(f'Os numeros adicionados foram {lista}')

''' PODEMOS USAR O COMANDO LIST(SET(variavel))
O comando SET remove os itens duplicados, e o LIST antes do SET é para transformar novamente em lista
DEIXANDO TUDO EM ORDEM CRESCENTE!'''

while True:
    n=int(input('Digite numeros até cansar: '))
    numeros.append(n)
    if n == 0:
        break
print(numeros)
numeros = list(set(numeros))
print(numeros)