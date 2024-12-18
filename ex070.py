total = prod1000 = 0
contador = prodmenor= 0
barato = ''
while True:
    produto = str(input('Nome do produto: ')).strip()
    valor = int(input('Valor do produto R$: '))
    contador+=1
    continuar = ' '
    while continuar not in 'SsNn':
        continuar = str(input('Deseja adicionais mais itens [S]-sim [N]-não: ')).strip().upper()[0]
    total += valor
    if contador == 1 or valor < prodmenor:
        prodmenor = valor
        barato = produto
    if valor < valor:
        maisbarato = produto
    if valor > 1000:
        prod1000 += 1
    if continuar == 'N':
        break
print(f'O total de produtos que custam mais de R$ é 1000,00 é {prod1000}.')
print(f'O total da compra é {total}')
print(f'O produto mais barato foi {barato}.')