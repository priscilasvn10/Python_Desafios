s =0
i = 0
m = 0
for c in range (1, 5):
    print('-'*5, ' {}ª PESSOA '.format(c),'-'*5)
    nome = str(input('Digite o nome: '))
    idade = int(input('Digite a idade: '))
    sexo = int(input('Digite o 1 para M e 2 para F: '))
    s +=idade
    if idade > i:
        i = idade
        n = nome
    if sexo == 2 and idade < 20:
         m +=1

print('A média das idades é: {}'.format(s/4))
print('{} é o homem mais velho'.format(n))
print('{} mulheres tem menos de 20 anos'.format(m))