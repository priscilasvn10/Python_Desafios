le = float(input('Digite a distância de uma viagem em Km: '))
if le <= 200:
    valor = le*0.50
    print('O valor da sua passagem é: R$ {}'.format(valor))
else:
    valor = le * 0.45
    print('O valor da sua passagem é: R$ {}'.format(valor))
