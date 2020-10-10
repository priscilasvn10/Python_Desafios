s =0
cont = 0
for c in range (1, 501, 2):
    if c%3 == 0:
        cont+=1
        s = s + c
print('A soma dos {} multiplos de 3 no intervalo de 1 até 500 é: {}'.format(cont,s))