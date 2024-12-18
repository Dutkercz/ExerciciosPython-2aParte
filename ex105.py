def notas(*n, sit=False):
    '''
    Função para guardar notas de alunos. e mostrar média
    :param n: valor de cada nota do aluno. sem limite de notas
    :param sit: se True > mostra situação do aluno, >7 = boa, >5 e <7 = razoável, <5 = péssima.(padrão False)
    :return: retorna uma lista com as informações
    '''
    lis = {}
    soma = sum(n)
    lis['Total'] = len(n)
    lis['Maior nota'] = max(n)
    lis['Menor nota'] = min(n)
    lis['Media'] = soma / len(n)
    if sit == True:
        if lis['Media'] >= 7:
            lis['Situação'] = 'Boa'
        elif 5 <= lis['Media'] < 7:
            lis['Situação'] = 'Razoável'
        else:
            lis['Sitação'] = 'Péssima'
    return lis



#PROGRAMA PRINCIPAL
resp = notas(4.5, 5.3, 3.5, 9.4, 1.5, 10, 10)
print(resp)
help(notas)