casa = float(input('Qual o valor da casa: R$ '))
sal = float(input('Salário do comprador: R$ '))
anos = int(input('Quantos anos de financiamento? '))

prestacao = casa/(anos * 12)
minimo = sal * 30 / 100

print('Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}'.format(casa, anos, prestacao))

if prestacao <= minimo:
    print('Empréstimo pode ser CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')
