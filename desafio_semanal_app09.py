'''
Faça um programa que leia um texto da web e depois ele te escreva de forma codificada 

Ex de codificação: A @ - E 3 - I 1 - O 0 - S $

'''
import os
from time import sleep
text = '''
        o que é um endereço IP?

        a explicação pode ficar bastante técnica, mas nós podemos resumir IP(sigla para Internet Protocol, ou “protocolo de internet”) como uma forma de atribuir uma identificação para todos os dispositivos conectados a uma rede, o que inclui notebooks, desktops, smartphones, impressoras e qualquer outra coisa que precise receber e enviar informações na rede.

'''
os.system('clear')
text1 = text.replace('a', '4')
text2 = text1.replace('e', '3')
text3 = text2.replace('i', '1')
text4 = text3.replace('o', '0')
text5 = text4.replace('s', '$')

for l in text5.upper():
    sleep(.02)
    print(l, end = '', flush = True)
# print(text5.upper())
