pre = float(input('Qual é o preço do produto? R$'))
a = pre - (pre*0.05)
print('O produto que custava R${:.2f}, na promoção com desconto de 5% vai custar R${:.2f}'.format(pre,a))