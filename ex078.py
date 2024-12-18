from operator import index

lista = []
maior = 0
menor = 0
for numlista in range (0,5):
    lista.append(int(input(f'Digite o valor para a posição {numlista+1}: ')))
    if numlista == 0:
        maior = lista[numlista]
        menor = lista[numlista]
    else:
        if lista[numlista] > maior:
            maior = lista[numlista]
        if lista[numlista] < menor:
            menor = lista[numlista]

print(f'Você digitou os valores {lista}')
print(f'O menor valor digitado foi {menor}, na posições: ',end=' ')
for posicao, valor in enumerate(lista):#para cada POSICAO, eu quero saber o VALOR de cada item da LISTA
    if valor == menor:# se o VALOR for igual ao menor numero:
        print(f'{posicao +1}...', end='') #vou PRINTAR A POSIÇÃO DELE .... VARRENDO TODA A MINHA LISTA ATÉ O ULTIMO VALOR
print(f'\nO maior valor digitado foi {maior}, nas posições: ', end='')
for posicao, valor in enumerate(lista):# PARA CADA POSICAO NA LISTA EU PEGO O SEU VALOR
    if valor == maior: #COM ESSE VALOR DA LISTA, EU COMPARO COM O MAIOR NUMERO
        print(f'{posicao +1}',end='...')#SE O VALOR NO LAÇO ATUAL FOR IGUAL, EU PRINTO SUA POSIÇÃO, ATÉ O FIM DA LISTA