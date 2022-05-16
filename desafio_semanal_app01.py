'''Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99 e agora possui uma loja de conveniências. 

- Faça um programa que implemente uma caixa registradora rudimentar. 
- O programa deverá receber um número desconhecido de valores referentes aos preços das mercadorias. 
- Um valor zero deve ser informado pelo operador para indicar o final da compra. 
- O programa deve então mostrar o total da compra e perguntar o valor em dinheiro que o cliente forneceu, para então calcular e mostrar o valor do troco. 
- Após esta operação, o programa deverá voltar ao ponto inicial, para registrar a próxima compra. 
- A saída deve ser conforme o exemplo acima:

=> Formas de pagamento que o programa deve ter 
    - dinheiro, 
    - crédito, 
    - débito,
    - pix
mas
    - Débito não tera desconto nem aumentọ
    - Crédito aumento de 3.54%
    - Dinheiro desconto de 3.12%
    - Pix desconto de 1.85%

Lembrando que se vc quiser fazer uma interface gráfica ou uma base de dados fique a vontade só não coloquei isso pq nem todos sabem fazer isso'''

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
