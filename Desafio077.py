palavras = ('aprender','programas', 'linguagem', 'python','curso', 'gratis',
            'estudar', 'praticar','trabalhar', 'mercado', 'programador', 'futuro')

for c in palavras:
    print(f'\nNa palavra \033[0;36m{c.upper()}\033[m temos ', end= '')
    for le in c:
        if le.lower() in 'aeiou':
            print(f'\033[0;36m {le}\033[m', end=' ')
