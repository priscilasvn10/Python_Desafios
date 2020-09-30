# calcule o preço da passagem, cobrando 0,50 centavos por km para viagens at´r 200 km e 0,45 centavos para viagens mais longas
le = float(input('Digite a distância de uma viagem em Km: '))
if le <= 200:
    valor = le*0.50
    print('O valor da sua passagem é: R$ {}'.format(valor))
else:
    valor = le * 0.45
    print('O valor da sua passagem é: R$ {}'.format(valor))
