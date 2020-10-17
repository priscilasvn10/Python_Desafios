cont = 0
print('='*30)
print('{:^30}'.format('Banco PP'))
print('='*30)
val = int(input('Digite o valor do Saque: R$ '))
qunTem = val
cedula = 50
cont = 0
while True:
    if qunTem >= cedula:
        qunTem -= cedula
        cont += 1
    else:
        if cont > 0:
            print(f'Foi necessário {cont} cédulas de R${cedula}.')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        cont = 0
        if qunTem == 0:
            break

print('='*30)
print('Volte sempre ao BANCO PP')
