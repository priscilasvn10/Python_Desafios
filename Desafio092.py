from datetime import date
dados = {}
ano_atual = date.today()
dados['nome'] = str(input('Nome: '))
ano = int(input('Ano de Nascimento: '))
idade = ano_atual.year - ano
dados['idade'] = idade
dados['ctps'] = int(input('Carteira de trabalho (0 não tem): '))
if dados["ctps"] != 0:
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['salário'] = float(input('Salário: R$ '))
    dados['Aposentadoria'] = (35 - (ano_atual.year - dados["contratação"]))+dados["idade"]
    print('='*30)
for k, v in dados.items():
    print(f'{k} tem o valor {v}')
