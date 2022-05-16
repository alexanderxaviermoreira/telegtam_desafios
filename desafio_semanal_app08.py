'''
Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;
'''
import os

res1 = 'A equação não é do Segundo Grau.'
res2 = 'Não há raízes reais.'
res3 = 'Possui apenas uma raiz real.'
res4 = 'Possui duas raiz reais'
os.system('clear')
print('ax² + bx + c = 0')
a = int(input('\nValor de "A": '))
if a == 0:
    print(res1.center(50), '\n')
else:
    b = int(input('\nValor de "B": '))
    c = int(input('\nValor de "C": '))
    delta = pow(b,2) - 4 * a * c
    os.system('clear')
    print(f'\nValor de Delta: {delta}.')
    if delta < 0:
        print(res2.center(50), '\n')
    elif delta == 0:
        print(res3.center(50), '\n')
    elif delta >= 0:
        print(res4.center(50), '\n')
