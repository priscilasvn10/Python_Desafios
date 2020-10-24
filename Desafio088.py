from random import randint
from time import sleep
matriz = []
cont = 1
print('-'*40)
print(f'Joguinho do Sorteio')
print('-'*40)
x = int(input('Quantos jogos você deseja sortear? '))
print('='*5, end='')
print(f' Sorteando {x} jogos ', end='')
print('='*5,'\n')

for j in range(1,x+1):
    while True:
         jo = randint(1, 60)
         if jo not in matriz:
            matriz.append(jo)
            cont += 1
         if cont >= 7:
             break
    matriz.sort()
    print(f'Jogo {j}: {matriz} ')
    sleep(1)
    matriz.clear()
    cont = 1
print('='*5, end='')
print(' < Boa sorte > ', end='')
print('='*5)
