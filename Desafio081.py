'''ler vários números e colocar na lista
a) quantos números foram digitados
b)ordem decrescente
c)se o valor 5 foi digitado e está ou não
na lista'''

num = []
i = 0
while True:
    num.append(int(input('Digite um número: ')))
    c = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if c == 'N':
       break
print('='*30)
print(f'Foram digitados {len(num)} números.')
num.sort(reverse=True)
print(f'A ordem decrescente é: {num}')
if 5 in num:
    print('O valor 5 foi digitado na lista.')
else:
    print('O valor 5 não foi digitado na lista.')