num = []
for i in range(0, 5):
    n = int(input('Digite um valor: '))
    if i == 0 or n > num[-1]:
        num.append(n)
        print('Adicionado ao final da lista.')
    else:
        cont = 0
        while cont < len(num):
             if n <= num[cont]:
                num.insert(cont, n)
                print(f'Adicionado na posição {cont} da lista.')
                break
             cont += 1
print('='*40)
print(f'A lista ordenada é: {num}')




