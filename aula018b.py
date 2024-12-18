teste = list()
teste.append('gustavo')
teste.append(40)
galera = list()
galera.append(teste[:])# adiciono 'gustavo','40'
teste[0] = 'maria'#troquei 'gustavo' por 'maria'
teste[1] = 22#tambem troquei '40' por '22'
galera.append(teste[:])#como as possições trocada, a lista
#'galera' tambem irá trocar suas informações
print(galera)
print()
print()
turma = [['cris',32], ['jenifer',29], ['alvaro',5], ['maria',2]]
print(turma)#mostra todos mundo
print(turma[0])#mostra só cris,32
print(turma[0][0])#mostra só o 32
#usando o for para mostrar só nome ou a idade
for pes in turma:
    #print(pes)# mostra um por linha 'nome' e 'idade'
    #print(pes[0])#mostra só os nome, ou item na possição 0
    #print(pes[1])#nesse causo ira mostrar só a idade
    print(f'{pes[0]} tem {pes[1]} anos de idade')
    