'''vários valores na lista, se o numero estiver
na lista não
(aceitará)no final mostar os
numeros em ordem crescente'''
num =[]
i=0
while True:
    n = int(input('Digite um valor: '))
    if n not in num:
        num.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')

    d = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
    if d =='N':
        break
print('='*30)
num.sort()
print(f'Os valores digitados foram: {num}')
