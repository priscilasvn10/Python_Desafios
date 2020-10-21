'''leia 5 valore e guarde na lista
mostrar o maior e o menor valor digitados
e suas posiçoes na lista'''

num = []
for i in range(0, 5):
    num.append(int(input(f'Digite o valor na posição {i}: ')))
    if i == 0:
        maior = menor = num[i]
    else:
        if maior < num[i]:
            maior = num[i]
            cont = i
        elif menor > num[i]:
            menor = num[i]
            cont1 = i
print('=-'*30)
print(f'Você digitou os valores {num}')
print(f'O maior valor é {maior} nas posições ', end='')
for c , v in enumerate(num):
    if v == maior:
        print(f'{c}...', end='')
print()
print(f'O menor valor é {menor} nas posições ', end='')
for c,v in enumerate(num):
    if v == menor:
        print(f'{c}...', end='')
