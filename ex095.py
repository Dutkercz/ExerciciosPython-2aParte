jogador = {}
gols = []
grupo = []
while True:
    gols.clear()
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: ')).strip().title()
    np = int(input(f'Numero de partidas do jogador {jogador["nome"]}: '))
    for c in range (0, np):
        gols.append(int(input(f'    Numero de gols na {c+1} partida: ')))
    jogador['gols'] = gols[:]
    jogador['total']=sum(gols)
    grupo.append(jogador.copy())
    while True:
        continuar = str(input('Deseja continuar [S/N]')).strip().upper()[0]
        if continuar in 'SN':
            break
        else:
            print('OPÇÃO INVÁLIDA, RESPONDA S ou N')
    if continuar == 'N':
            break
print(grupo)
print(f'{'Cod':<4}{'Nome':^9}{'Gols':^18}{'Total':^25}')
for i, v in enumerate(grupo):
    print(f'{i:>2}', end='')
    for valk in v.values():
        print(f'{str(valk):^14}', end='   ')#usar str, pois se for numero não ira formatar os espaços
    print()

while True:
    info = int(input('Para mais informações digite o código: \033[31m[999 - PARAR]\033[m'))
    if info == 999:
        break
    if info >= len(grupo):
        print(f'NÃO FOI ENCONTRADO JOGADOR COM O CÓDIGO {info}')
    else:
        print(f'--> \033[32mLevantamento do jogador {grupo[info]["nome"]}\033[m')
        for c, v in enumerate (grupo[info]['gols']):
            print(f'Na partida {c+1}, fez {v} gols')
print('\033[31m PROGRAMA FINALIZADO\033[m')
