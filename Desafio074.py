from random import randint
n = (randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10) )
print(f'Valores sorteados foram: ', end='')
for num in n:
    print(f'{num} ', end='')
print(f'\nO maior valor sorteado foi {max(n)}')
print(f'O menor valor sorteados foi {min(n)}')
