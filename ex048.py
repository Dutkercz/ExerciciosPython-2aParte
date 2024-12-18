print('CALCULAR A SOMA DE TODOS OS NÚMEROS IMPARES DIVISIVEIS POR 3, ENTRE 1 - 500')
soma = 0
contador = 0
for c in range(1,501, 2):
    if c % 3 == 0:
        contador = contador+1 # pode usar > contador += 1
        soma = soma + c #pode usar > soma += c (tem que cuidar a indentação)
print('A soma de todos os {} valores selecionados é {}'.format(contador, soma)) #cuidar indentação