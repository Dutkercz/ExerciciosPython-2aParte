
turma= list()
dados = list()
for c in range (0,3):
    dados.append(str(input('digite seu nome: ')))
    dados.append(int(input('Digite sua idade: ')))
    turma.append(dados[:])#cria um copia temporaria para nao terem ligação
    dados.clear()#apaga os dados da lista dados
print(turma)
for p in turma:
    if p[1] >= 21:
        print(f'{p[0]} é MAIOR DE IDADE')
    else:
        print(f'{p[0]} é MENOR DE IDADE')
        