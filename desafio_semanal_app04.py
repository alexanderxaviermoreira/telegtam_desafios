'''
Faça um programa que converta da notação de 24 horas para a notação de 12 horas. Por exemplo, o programa deve converter 14:25 em 2:25 P.M. A entrada é dada em dois inteiros. Deve haver pelo menos duas funções: uma para fazer a conversão e uma para a saída. Registre a informação A.M./P.M. como um valor ‘A’ para A.M. e ‘P’ para P.M. Assim, a função para efetuar as conversões terá um parâmetro formal para registrar se é A.M. ou P.M. Inclua um loop que permita que o usuário repita esse cálculo para novos valores de entrada todas as vezes que desejar.
'''
import os

def cabecalho():
    os.system('clear')
    print('\n{:^40}'.format('#'*38))
    print('{:^40}'.format('#        CONVERSOR DE NOTAÇÃO        #'))
    print('{:^40}\n'.format('#'*38))

def conversao(h, m):
    if h <= 12 and m <= 59:
        print(f'\t\t{h}:{m} A.M.')
    elif h >= 12 and m <= 59:
        print(f'\t\t{h - 12}:{m} P.M.')

        
cabecalho()
while True:
    horas = int(input('\tHORAS: '))
    minutos = int(input('\tMINUTOS: '))
    conversao(horas, minutos)



