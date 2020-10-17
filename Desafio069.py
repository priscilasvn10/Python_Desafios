cont = m = f = 0
while True:
    idade =  int(input('Digite uma idade: '))
    if idade >= 18:
        cont += 1
    sexo = ' '
    while sexo not in 'FM':
        sexo = str(input('Digite o sexo: [F/M] ')).upper().strip()[0]
        if sexo == 'M':
            m += 1
        if idade < 20 and sexo == 'F':
            f += 1
        s = ' '
    while s not in 'SN':
        s = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    print('='*30)
    if s == 'N':
        break
print(f'Foram {cont} pessoas maiores de 18 anos.')
print(f'Temos {m} homens cadastrados.')
print(f'E temos {f} mulheres com menos de 20 anos.')
