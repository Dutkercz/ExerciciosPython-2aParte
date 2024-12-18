

listaPalavras = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'VIDEO',
            'GRATIS', 'ESTUDAR', 'PRATICAR', 'TRABALHAR','MERCADO', 'FUTURO', 'PROGRAMADOR')
for PALAVRA in listaPalavras:
    print('\n',PALAVRA, end=' ')
    for letra in PALAVRA: # A PALAVRA SE TORNA UM LISTA COM TODAS AS SUAS LETRAS, E POMODES TESTAR CADA UMA DELAS
        if letra.lower() in 'aeiou': # EX: CURSO SE TORNA C,U,R,S,O  o laço FOR vai testar cada uma das letras
            print(letra.lower(), end=' ') # se LETRA estiver dentro da condição do IF ela será printada
print()
print()
for posicao in listaPalavras:
    print(f'\nNa palavra {posicao} temos as vogais', end=': ')
    for letra in posicao:
        if letra.lower() in 'aeiou':
            print(letra.lower(), end=' ')