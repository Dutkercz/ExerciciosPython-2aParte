print('Detector de Palíndromo')
frase = str(input('Digite uma frase: ')).strip().upper()
frase = frase.split()
junta = ''.join(frase)
inverso = '' #declarar uma variavel 'vazia' que vai servir como contador, para acumular as letras.
for c in range (len(junta)-1, -1, -1):
    inverso += (junta[c]) #Aqui começa a acumlar letra por letra, formando a palavra ao contrario.
if junta == inverso: #Com a variável 'junta' declarada no inicio do alg. foi poissivel fazer a comparação
    print('TEMOS UM PALÍNDROMO!')
else:
    print('Não temos um PALÍNDROMO!')