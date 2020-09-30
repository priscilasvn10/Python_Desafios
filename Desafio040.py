n1 = float(input('Digite a Primeira nota: '))
n2 = float(input('Digite a Segunda nota: '))

media = (n1+n2)/2

if media <5.0:
    print('Reprovado!')
elif media >=5 and media <= 6.9:
    print('Recuperação!')
else:
    print('Aprovado!')

