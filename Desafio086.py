total = [[0,0,0],[0,0,0],[0,0,0]]
for l in range (0,3):
    for c in range (0,3):
        total[l][c] = int(input(f'Digite um valor para [{l}][{c}]: '))
print('='*40)

for l in range (0,3):
    print()
    for c in range (0,3):
         print(f'[ {total[l][c]:^5} ] ', end='')