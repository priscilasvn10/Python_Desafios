def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mErro: por favor, digite um número inteiro válido.\033[m ')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n


def linha(tam = 42):
    return print('-'*tam)


def cabeçalho(texto):
    linha()
    print(texto.center(42))
    linha()


def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    c =1
    for itens in lista:
        print(f'\033[33m{c}\033[m -\t\033[34m{itens}\033[m')
        c+=1
    linha()
    n = leiaInt('\033[32mSua Opção:\033[m ')
    return n


