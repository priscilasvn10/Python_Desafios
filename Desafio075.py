'''leia 4 valores e guarde na tupla
a)quantas vezes o 9 apareceu
b) em que posição foi digitado o primeiro 3
c) quais foram os números pares'''

num = (int(input('Digite o primeiro valor: ')), int(input('Digite o segundo valor: ')),
       int(input('Digite o terceiro valor: ')), int(input('Digite o quarto valor: ')))
print(f'O número 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'O número 3 está {num.index(3)+1}° posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
print('O números pares forão: ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')
