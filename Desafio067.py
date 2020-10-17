print('='*30)
print('TABUADA')
while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    if n < 0:
        break
    for cont in range(1, 11):
        print(f' {n} x {cont} = {n*cont}')
    print('='*30)
print('Programa de tabuada encerrada. volte sempre!')
