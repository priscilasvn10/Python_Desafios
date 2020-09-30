d = int(input('Quantos dias alugados? '))
ro = float(input('Quantos Km rodados? '))
pre = (60 * d) + (0.15*ro)

print('O total a pagar é de R${:.2f}'.format(pre))