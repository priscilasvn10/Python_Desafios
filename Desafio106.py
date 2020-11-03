from time import sleep
c = ('\033[m',          #0- sem cores
     '\033[0;30;41m',   #1- vermelho
     '\033[0;30;42m',   #2- verde
     '\033[0;30;43m',   #3- amarelo
     '\033[0;30;44m',   #4- azul
     '\033[0;30;45m',   #5- roxo
     '\033[7;30m'       #6- branco
      );

def ajuda(com):
    print(c[2],end='')
    titulo(f'Acessando o manual do comando \'{com}\'',4)
    print(c[6],end='')
    help(com)
    print(c[0],end='')
    sleep(2)


def titulo(msg, cor=0):
    tam = len(msg)+4
    print('~'*tam)
    print(f'  {msg}')
    print('~'*tam)
    print(c[0],end='')
    sleep(1)


#programa principal
comando = ''
while True:
    print(c[3],end='')
    titulo('SISTEMA DE AJUDA PyHELP',2)
    print(c[0],end='')
    comando = str(input("Função ou Biblioteca > "))
    if comando.upper() == 'FIM':
        print(c[1],end='')
        break
    else:
        ajuda(comando)

titulo('ATÉ LOGO!',1)