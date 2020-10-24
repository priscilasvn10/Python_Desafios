boletim = []
while True:
    nome = str(input('Digite o nome do aluno: '))
    n1 = float(input('Digite a 1° nota: '))
    n2 = float(input('Digite a 2° nota: '))
    media = (n1+n2)/2
    boletim.append([nome, [n1,n2],media])
    print(boletim)
    res = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
    if res in 'N':
        break
print(f'\n{"Cod":<6}{"Nome":<10}{"Média":>7}')
print('-'*30)
for x in range(len(boletim)):
    print(f'{x:<6}{boletim[x][0]:<10}{boletim[x][2]:>7}')
print('-'*30)
while True:
    no = int(input('Mostrar notas de qual aluno? (999 Sair) '))
    if no == 999:
        break
    else:
        print(f'Notas de {boletim[no][0]} são: {boletim[no][1]}')
    print('-' * 30)
print('-' * 30)
print('Volte sempre!')
