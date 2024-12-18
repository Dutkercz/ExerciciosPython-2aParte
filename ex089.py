boletim = []
while True:
    nome = str(input('Digite o nome do aluno: '))
    n1 = float(input('Digite a 1a nota do aluno: '))
    n2 = float(input('Digite a 2a nota do aluno: '))
    media = (n1 + n2) / 2
    boletim.append([nome, [n1, n2], media])
    cont = str(input('Deseja adicionar mais alunos? [S] / [N]: ')).strip().upper()[0]
    if cont == 'N':
        break

print(f'{'No':<.5}    {'Aluno':^.10}    {'Média':>.20}')
for v , i in enumerate (boletim):
    print(f'{v}    {i[0]:<12}    {i[2]:<10}')
while True:
    op = int(input('Deseja ver as notas de qual aluno: [999] para encerrar '))
    if op < 999:
        print(f'Aluno {boletim[op][0]} notas {boletim[op][1]}')
    else:
        break