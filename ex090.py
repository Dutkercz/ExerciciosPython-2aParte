alunos = {}

alunos['Nome'] = str(input('Digite o nome do Aluno: ')).strip().title()
alunos['Media'] = float(input(f'Digite a média do Aluno {alunos["Nome"]}: '))
if alunos['Media'] >= 7:
    alunos['Situação']= 'APROVADO'
elif alunos['Media'] < 7:
    alunos['Situação']= 'REPROVADO'
for key, val_K in alunos.items():
    print(f'{key} é: {val_K}')