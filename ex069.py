contadorH = 0
contadorMaior = 0
mulheres20 = 0
while True:
    print('====='*15)
    #nome = str(input('Digite o nome do usúario: ')).strip().title()
    idade = int(input('Digite a idade do usúario: '))
    sexo = str(input('Digite o sexo do usúario [M/F]: ')).strip().lower()[0]
    continuar = str(input('Deseja continuar o cadastro? [S] - [N]: ')).strip().lower()[0]
    print('=====' * 15)
    if idade != int and sexo not in 'MmFf':
        print('\033[31mInformações invalidas, revise sua respostas!\033[m')
        print('=====' * 15)
    else:
        #print(f'Cadastro de {nome} concluido!')
        if idade > 18 :
            contadorMaior += 1
        if sexo == 'm':
            contadorH += 1
        if sexo == 'f' and idade < 20:
            mulheres20 += 1
        if continuar == 'n':
            break
print('CADASTROS CONCLÚIDOS')
print(f'Foram cadastrados {contadorH} Homens.')
print(f'Foram cadastrados {contadorMaior} pessoas maiores de 18 anos.')
print(f'Foram cadastradas {mulheres20} mulheres com menos de 20 anos.')