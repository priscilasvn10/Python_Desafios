print('='*11, ' Loja X ', '='*11)
n = float(input('Preço das compras: R$ '))
print('FORMAS DE PAGAMENTO')
print(' [ 1 ] à vista dinheiro/cheque\n [ 2 ] à vista cartão\n [ 3 ] 2x no cartão\n [ 4 ] 3x ou mais no cartão ')
x = int(input('Qual é a opção de pagamento? '))

if x == 1:
    desconto = n - (n*10/100)
elif x == 2:
    desconto = n - (n*5/100)
elif x ==3:
    desconto = n
    total = desconto / 2
    print('Sua compra será de 2x de R${:.2f} SEM JUROS '.format( total))
elif x == 4:
    desconto = n + (n*20/100)
    par = int(input('Quantas parcelas? '))
    total = desconto/par
    print('Sua compra será de {}x de R${:.2f} COM JUROS '.format(par,total))
else:
    desconto = n
    print('Opção inválida. Tente novamente!')
print('Sua compra de R$ {:.2f} vai custar R$ {:.2f} no final.'.format(n, desconto))