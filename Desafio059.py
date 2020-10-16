n=0
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
while n != 5:

    print('Escolha uma das opções abaixo:')
    n = int(input('[1] Somar \n[2] Multiplicar \n[3] Maior \n[4] Novos números \n[5] Sair do programa \n Qual a sua opção: '))
    if n == 1:
        print('A soma entre {} + {} = {}'.format(n1,n2,n1+n2) )
    elif n ==2:
        print('A multiplicação entre {} * {} = {}'.format(n1,n2,n1*n2))
    elif n == 3 :
        if n1 > n2:
            print('O maior número é {}'.format(n1))
        else:
            print('O maior número é {}'.format(n2))
    elif n == 4:
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))
    elif n == 5:
        print('Finalizando...')
    else:
        print('Opção inválida!. Tente novamente')
    print('=-'*20)
print('Acabou!')


