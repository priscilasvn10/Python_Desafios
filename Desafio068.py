from random import randint
vitoria = 0
while True:
    print('='*30)
    val = int(input('Diga um valor: '))
    computador = randint(0, 10)
    soma = computador + val
    escolha = ' '
    while escolha not in 'PI':
        escolha = str(input('Par ou Ímpar? [P/I]: ')).strip().upper()[0]
    print(f'Você jogou {val} e o computador {computador}. Total de {soma} ', end='')
    print('DEU PAR!' if soma %2 == 0 else 'DEU ÍMPAR')
    if escolha == 'P':
        if soma % 2 == 0:
            print('Você VENCEU!')
            vitoria += 1
        else:
            print('Você PERDEU!')
            break
    elif escolha == 'I':
        if soma % 2 != 0:
            print('Você VENCEU!')
            vitoria += 1
        else:
            print('Você PERDEU!')
            break
    print('Vamos jpgar novamente...')
print(f'GAME OVER! Você Ganhou {vitoria} vezes.')

