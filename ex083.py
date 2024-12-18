parentA = []
parentF = []
contA = 0
contB = 0
pilha = []

equ = input('Digite a sua equação para valida-la!: ')
for c in range (0,len(equ)):
    if '(' in equ[c]:
        parentA.insert(c,'(')
        contA +=1
    elif ')' in equ[c]:
        parentF.insert(c, ')')
        contB += 1
print(contA, contB)
if contA == contB:
    print('Sua Equação é VÁLIDA!!')
elif contA != contB:
    print('Sua equação é INVÁLIDA!')

for c in equ:
    if c == '(':
        pilha.append(c) #se for um '(' ele adiciona na pilha
    elif c == ')': #se não for um '(' ele verificar se é um ')'
        if len(pilha) > 0: # se for um ')' ele entra nesse laço, enquanto o tamanho da pilha com '(' for > 0
            pilha.pop() #apaga o ')' para igualar a PILHA
        else: # se o tamanho da pilha que contem os '(' for == 0
            pilha.append(')')# ele adiciona um ')' indicando que os '(' ')' não estão iguais
            break #para de percorrer o laço
if len(pilha) == 0:
    print('sua expressão esta valida')
else:
    print('Sua equação está errada!')