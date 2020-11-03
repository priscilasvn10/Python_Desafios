def leiaInt(num):
    ok = False
    valor = 0
    while True:
        n = str(input(num))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[031mErro! Digitar um número válido.\033[m')
        if ok:
            break
    return valor


print('-'*30)
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
