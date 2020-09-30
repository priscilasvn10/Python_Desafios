velo = float(input('Digite a velocidade do carro em Km: '))

if velo >=80:
    mult = velo*7.00
    print('Você recebeu uma multa do valor de R$ {}'.format(mult))