boletim = {}
boletim['nome'] = str(input('Nome: '))
boletim['média'] = float(input(f'Média de {boletim["nome"]}: '))
if boletim['média'] >= 7:
    boletim['situação'] = 'Aprovado'
elif 5 <= boletim['média'] < 7:
    boletim['situação'] = 'Recuperação'
else:
    boletim['situação'] = 'Reprovado'
print('='*30)
for e in boletim:
    print(f'{e} é igual a {boletim[e]}')
