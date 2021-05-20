from colorama import Fore, Style, Back
from random import randint
import time


def gera_numero():
    num_gerado = randint(1, 100)
    print(Fore.YELLOW + 'Pensando em um número de 1 a 100\n', Style.RESET_ALL)
    time.sleep(1)
    return num_gerado


def menu():
    print(Fore.BLACK, Back.LIGHTGREEN_EX + '-=' * 30, Style.RESET_ALL)
    print(Fore.CYAN + '\033[1mAcerte o número\033[0m'.center(60))
    print(Fore.CYAN + 'Aperte enter para iniciar o jogo!'.center(60), Style.RESET_ALL)
    print(Fore.BLACK, Back.LIGHTGREEN_EX + '-=' * 30, Style.RESET_ALL)


menu()
enter = input()
if enter == '':
    num = gera_numero()
    tentativas = 0
    while True:
        resposta = int(input('Qual número eu pensei: '))
        time.sleep(1)
        if resposta == num:
            tentativas += 1
            print('Parabens você acertou o número com', Fore.RED + f'{tentativas} tentativas\n', Style.RESET_ALL)
            jogar_dnv = input(Fore.GREEN + 'Quer jogar mais uma rodada(S/N): ')
            if jogar_dnv.lower()[0] == 's':
                num = gera_numero()
                tentativas = 0
            else:
                exit()
        elif resposta > num:
            print('O número que eu pensei é', Fore.RED + 'menor', Style.RESET_ALL)

            tentativas += 1
        elif resposta < num:
            print('O número que eu pensei é', Fore.RED + 'maior', Style.RESET_ALL)
            tentativas += 1
