dados = {}
pessoas = []
cont = 0
while True:
    dados.clear()
    dados['nome'] = str(input('Nome: '))
    while True:
        dados['sexo'] = str(input('Sexo:[M/F] ')).upper().strip()[0]
        if dados['sexo'] in 'MF':
             break
        print('Erro! Por favor, digite apenas M ou F.')
    dados['idade'] = int(input('Idade: '))
    pessoas.append(dados.copy())
    cont += dados["idade"]
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
        if resp in 'SN':
            break
        print('Erro! Por favor, digite apenas S ou N.')
    if resp == 'N':
        break
print('-='*30)
print(pessoas)
print(f'- O grupo tem {len(pessoas)} pessoas.')
media = cont/len(pessoas)
print(f'- A média de idade é de {media:.2f} anos.')
print(f'- As mulheres cadastradas foram: ', end='')
for v in pessoas:
    if v["sexo"] == 'F':
        print(f'{v["nome"]} ', end='')
print('\n- Lista das pessoas que estão acima da média: ')
for p in pessoas:
    if p["idade"] >= media:
        print('   ', end='')
        for k, v in p.items():
           print(f'{k} = {[v]}; ', end='')
        print()
print('<<< FIM >>>')
