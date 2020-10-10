#leia seis numeros e mostre a soma
#apenas daqueles que forem pares.
#se o valor digitado for impar desconsidere-o
s=0
cont = 0
for c in range (1,7):
    a = int(input('Digite o {} valor: '.format(c)))
    if a%2 ==0:
        s += a
        cont+=1
print('Foi informado {} valores e a soma dos Pares é: {}'.format(cont, s))
