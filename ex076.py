produtos = ('Lápis', 3.00, 'Caderno', 9.90,'Borracha',3.50,
            'Estojo',7.90, 'Transferidor',8.90, 'Compasso',12.50, 'Mochila',99.90,
            'Canetas',16.90,'Livros',79.90)
print('==='*20)
print(f'{'LISTAGEM DE PREÇOS':^50}')
print('==='*20)
for pos in range (0, len(produtos)):
    if pos % 2 == 0:
        print(f'{produtos[pos]:.<30}', end=' R$ ')
    elif pos % 2 == 1:
        print(f'{produtos[pos]:.2f}')
print('==='*20)