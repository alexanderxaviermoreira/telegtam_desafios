'''
Desafio da semana 
Desafio da mega - sena
O desafio consiste um fazer um programa que sorteia 6 números entre 0 a 60
Lembrando que os números não pode se repetir 
Ótimo desafio a todos
'''

from random import randint
from time import sleep
import os



palpites = []
sorteio = []

print()
print('-~'*20)
print('{:^40}'.format('SORTEIO DA MEGA SENA'))
print('-~'*20)


jogos = int(input('\nNúmero de jogos: '))
print('{:#^15}'.format(f'\nSerão gerados {jogos} jogos, com 6 números cada.'))
sleep(3)
os.system('clear')
sleep(1.5)
print()
while len(palpites) < jogos:
    n = randint(1, 60)
    if n not in sorteio:
        sorteio.append(n)
        if len(sorteio) == 6:
            palpites.append(sorted(sorteio[:]))
            sorteio.sort()
            sorteio.clear()
for e, j in enumerate(palpites):
    sleep(.25)
    print(f'- Jogo nr {e+1}: {j}')

print()
