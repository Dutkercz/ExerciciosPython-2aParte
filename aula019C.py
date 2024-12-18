brasil = []
estado = {}
for c in range(0,3):
    estado['UF'] = str(input('UNIDADE FEDERATIVA: '))
    estado['sigla'] = str(input('Sigla da UF: '))
    brasil.append(estado.copy()) # ira copiar o que existe, e adicionar novas informações (FATIAMENTO DA LISTA)
#print(brasil)
#ou usando o FOR
for est in brasil:#esse for é para a lista 'BRASIL'
    for k, v in est.items():#ira se referir ao item gerado da lista, no causo era a VARIAVEL 'ESTADO'
        print(f'{k}, {v}')
