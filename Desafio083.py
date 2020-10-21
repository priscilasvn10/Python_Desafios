fr = str(input('Digite uma expressão: '))
ler = []
for simbolo in fr:
    if simbolo == '(':
        ler.append('(')
    elif simbolo == ')':
           if len(ler) > 0:
               ler.pop()
           else:
               ler.append(')')
               break
if len(ler) == 0:
    print('Expressão válida!')
else:
    print('Expressão Inválida!')
