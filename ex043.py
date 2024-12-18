print('calculadora de IMC')
peso = float(input('Digite seu peso atual: (Kg) '))
altura = float(input('Digite a sua altura atual em: (m) '))
imc = peso / (altura ** 2)
print('Seu IMC é de {:.2f}'.format(imc), end=' ')
if imc < 18.5 :
    print('Seu IMC é {:.2f}, você está ABAIXO DO PESO!.'.format(imc))
elif imc >= 18.5 and imc < 25:
    print('Seu IMC é {:.2f}, você está no PESO IDEAL!'.format(imc))
elif imc >= 25 and imc < 30:
    print('Seu IMC é {:.2f}, você está com SOBREPESO.'.format(imc))
elif imc >= 30 and imc < 40:
    print('Seu IMC é {:.2f}, você está OBESO, cuide da sua saúde!'.format(imc))
elif imc >= 40 :
    print('Seu IMC é {:.2f}, você está com OBESISADE MÓRBIDA, procure ajuda médica URGENTE!'.format(imc))