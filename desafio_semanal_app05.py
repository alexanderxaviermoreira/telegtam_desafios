'''
Jogo de Craps.
Faça um programa que implemente um jogo de Craps. O jogador lança um par de dados, obtendo um valor entre 2 e 12. Se, na primeira jogada, você tirar 7 ou 11, você um "natural" e ganhou. Se você tirar 2, 3 ou 12 na primeira jogada, isto é chamado de "craps" e você perdeu. Se, na primeira jogada, você fez um 4, 5, 6, 8, 9 ou 10,este é seu "Ponto". Seu objetivo agora é continuar jogando os dados até tirar este número novamente. Você perde, no entanto, se tirar um 7 antes de tirar este Ponto novamente.
'''

from random import randint
from time import sleep
import os

os.system('clear')
def cabecalho():
    os.system('clear')
    print('{:^40}'.format('~'*40))
    print('{:^40}'.format('JOGO DE CRAPS'))
    print('{:^40}'.format('Desafio da Semana (23 Abr 2022)'))
    print('{:^40}'.format('~'*40))


natural = [7, 11]
craps = [2, 3, 12]
ponto = [4, 5, 6, 8, 9, 10]
primeira_jogada = []

while True:
    print('\n\tAguarde o início do jogo.....')
    sleep(3)
    os.system('clear')
    cabecalho()
    dado_um_jogada_um = randint(1, 6)
    dado_dois_jogada_um = randint(1, 6)
    jogada_um = dado_um_jogada_um + dado_dois_jogada_um
    primeira_jogada.append(jogada_um)

    if jogada_um in natural:
        sleep(1)
        print(f'\tSua primeira jogada foi {jogada_um}.\nVocê é um "NATURAL". Você ganhou!!!\n')
    elif jogada_um in craps:
        sleep(1)
        print(f'\tSua primeira jogada foi {jogada_um}.\nVocê é um "CRAPS". Você perdeu!!!\n')
    elif jogada_um in ponto:
        sleep(1)
        print(f'\tSua primeira jogada foi {jogada_um}.\nEsse é o seu "PONTO"\n')

    print('{:^40}'.format('~'*40))

    while True:
        dado_um_jogada_dois = randint(1, 6)
        dado_dois_jogada_dois = randint(1, 6)
        jogada_dois = dado_um_jogada_dois + dado_dois_jogada_dois
        if jogada_dois == 7:
            sleep(1)
            print(f'\tSua segunda jogada foi {jogada_dois}\nVocê perdeu!!!\n')
            break
        elif jogada_dois in primeira_jogada:
            sleep(1)
            print(f'\tSua segunda jogada foi {jogada_dois}\nVocê ganhou!!!\n')
            break
    primeira_jogada.clear()
    print('{:^40}'.format('~'*40))
    print(primeira_jogada)
