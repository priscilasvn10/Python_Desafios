sair = 'S'
cont = soma =  maior = menor = 0
while sair != 'N':
    n = int(input('Digite um número: '))
    sair = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    cont += 1
    soma += n
    if cont == 1:
        maior = menor = n
    else:
        if maior < n :
            maior = n
        if menor > n:
            menor = n
print('Você digitou {} número e a média foi {:.2f}'.format(cont,soma/cont))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))
