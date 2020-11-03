def voto(n):
    from datetime import date
    ano_atual = date.today().year
    idade = ano_atual - n
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA.'
    elif idade >= 18 and idade < 65:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO.'
    else:
       return f'Com {idade} anos: VOTO OPCIONAL.'


#programa principal
print('-'*20)
n = int(input('Em que ano você nasceu? '))
print(voto(n))

