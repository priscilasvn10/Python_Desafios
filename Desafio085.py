total = [[],[]]
for c in range(1, 8):
    x = int(input(f'Digite o {c}° valor: '))
    if x % 2 == 0:
        total[0].append(x)
    else:
      total[1].append(x)
total[0].sort()
total[1].sort()
print('='*40)
print(f'Valores Pares {total[0]} \nValores Impares {total[1]}')