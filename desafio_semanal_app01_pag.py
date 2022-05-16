import PySimpleGUI as sg

sg.theme('DarkAmber')
layout = [
    [sg.Text('Para uso do reponsável pelo caixa')]
]

window = sg.Window('Caixa Registradora', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break
    print('You Entered', values(0))
window.close()



import os
from time import sleep

dados = []
compra = {}
valores = []

def cabecalho():
    print('-~'*15)
    print('{:^30}'.format('CAIXA REGISTRADORA'))
    print('-~'*15)

def opcoes():
    print('''
        Formas de pagamento:
            a) Espécie 
            b) Cartão de Crédito 
            c) Cartão de Débito
            d) PIX 
            ''')

def comprar():
    while True:
        compra['produto'] = input('\nProduto: ').upper()
        compra['valor'] = float(input('Valor: R$ '))
        valores.append(compra['valor'])
        dados.append(compra.copy())
        continuar = int(input('- 0 = Parar\t- 1 = Continuar: '))
        if continuar == 1:
            continue
        elif continuar == 0:
            break

def listar():
    print()
    for d in dados:
        for k, v in d.items():
            print(f'{k} - {v}')

def encerrado():
    print()
    print('#'*24)
    print('{:^24}'.format('COMPRA ENCERRADA'))
    print('#'*24)
    sleep(5)
    os.system('clear')


while True:
    os.system('clear')
    cabecalho()
    comprar()
    total = sum(valores)
    print(f'\n- Total da compra foi: R$ {total:.2f}')

    opcoes()

    forma_Pagamento = input('- Forma de pagamento: ')
    if forma_Pagamento == 'a':
        print('- Desconto de 3.12%')
        valor_Cliente = float(input('- Quanto o cliente forneceu ao caixa: '))
        troco_Sem_Desconto = valor_Cliente - total
        print(f'- Troco sem o desconto: R$ {troco_Sem_Desconto:.2f}')
        desconto = (total / 100) * 3.12
        print(f'- Desconto: R$ {desconto:.2f}')
        troco_Com_Desconto = valor_Cliente - (total - desconto)
        print(f'- Troco com desconto: R$ {troco_Com_Desconto:.2f}')

        listar()

        continuar = input('\n\tDeseja receber outra compra [s] ou [n]: ').upper()
        if continuar in 'sS':
            continue
        elif continuar in 'nN':
            encerrado()
            break

    elif forma_Pagamento == 'b':
        print('- Acréscimo de 3.54%')
        valor_Cliente=float(input('- Quanto o cliente forneceu ao caixa: '))
        troco_Sem_Acrescimo = valor_Cliente - total
        print(f'- Troco sem acréscimo: {troco_Sem_Acrescimo:.2f}')
        acrescimo = (total / 100) * 3.54
        print(f'- Acŕescimo: R$ {acrescimo:.2f}')
        troco_Com_Acrescimo = valor_Cliente - (total + acrescimo)
        print(f'- Troco com acréscimo: R$ {troco_Com_Acrescimo:.2f}')

        listar()

        continuar = input('\n\tDeseja receber outra compra [s] ou [n]: ').upper()
        if continuar in 'sS':
            continue
        elif continuar in 'nN':
            encerrado()
            break
        
    elif forma_Pagamento == 'c':
        print('- Sem alteração')
        valor_Cliente = float(input('- Quanto o cliente forneceu ao caixa: '))
        troco_Sem_Acrescimo = valor_Cliente - total
        print(f'- Troco sem acréscimo: {troco_Sem_Acrescimo:.2f}')

        listar()

        continuar = input('\n\tDeseja receber outra compra [s] ou [n]: ').upper()
        if continuar in 'sS':
            continue
        elif continuar in 'nN':
            encerrado()
            break
    
    elif forma_Pagamento == 'd':
        print('- Desconto de 1.85%')
        valor_Cliente = float(input('- Quanto o cliente forneceu ao caixa: '))
        troco_Sem_Desconto = valor_Cliente - total
        print(f'- Troco sem o desconto: R$ {troco_Sem_Desconto:.2f}')
        desconto = (total / 100) * 1.85
        print(f'- Desconto: R$ {desconto:.2f}')
        troco_Com_Desconto = valor_Cliente - (total - desconto)
        print(f'- Troco com desconto: R$ {troco_Com_Desconto:.2f}')

        listar()

        continuar = input('\n\tDeseja receber outra compra [s] ou [n]: ').upper()
        if continuar in 'sS':
            continue
        elif continuar in 'nN':
            encerrado()
            break
