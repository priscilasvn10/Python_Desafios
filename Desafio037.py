n = int(input('Digite um número inteiro: '))
print('Escolha uma das bases para conversão:')
print(' [ 1 ] converter para BINÁRIO \n [ 2 ] converter para OCTAL \n [ 3 ] converter HEXADECIMAL')

x = int(input('Sua opção: '))
if x == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(n,bin(n)[2:]))
elif x == 2:
    print('{} convertido para OCTAL é igual a {}'.format(n,oct(n)[2:]))
elif x == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(n,hex(n)[2:]))
else:
    print('Opção inválida. Tente novamente!')