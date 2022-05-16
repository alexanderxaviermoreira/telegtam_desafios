'''
Tabela de descontos por unidade de profuto:

    Quantidade          Desconto
    - até 9             - 0%
    - 10 a 99           - 5%
    - 100 a 999         - 10%
    - 1000 e acima      - 15%
'''
# - Inputo nome do Cliente
# - Input valor Unitário
# - Input Quantidade
# - Saída 1: Total s/ desconto
# - Saída 2: Total c/ desconto

import os

os.system('clear')
title = 'COMPRAS'
print('{:^20}'.format('\033[1m'+title+'\033[0m'))


produtos = ['arroz', 'feijão', 'óleo de soja', 'sal', 'açúcar', 'café', 'molho de tomate', 'macarrão', 'milho', 'farinha de trigo', 'farinha de mandioca', 'leite', 'manteiga', 'chá', 'carnes', 'peixes', 'ovos']

# os.system('clear')
continuar = ''
compra = []
dados = {}

while continuar in 'sS':    
    dados['Cliente'] = input('\nNome: ')
    print('\tLista de Produtos:\n')
    for e, p in enumerate(produtos):
        print(f'{e+1} - {p}')    
    dados['Produto'] = input('Produto: ')    
    if dados['Produto'] not in produtos:
        print('\tProduto inexistente.')
        continue
    dados['VU'] = float(input('Valor Unitário: '))
    dados['Qtde'] = int(input('Quantidade: '))
    dados['Total Sem Desconto'] = dados['VU'] * dados['Qtde']
    if dados['Qtde'] <= 9:
        dados['Total Sem Desconto']
    elif 99 <= dados['Qtde'] >= 10:
        dados['Total Com Desconto'] = dados['Total Sem Desconto'] - (dados['Total Sem Desconto'] / 100) * 5
    elif 999 <= dados['Qtde'] >= 100:
        dados['Total Com Desconto'] = dados['Total Sem Desconto'] - (dados['Total Sem Desconto'] / 100) * 10
    elif dados['Qtde'] >= 1000:
        dados['Total Com Desconto'] = dados['Total Sem Desconto'] - (dados['Total Sem Desconto'] / 100) * 15

    compra.append(dados.copy())
    continuar = input('Continuar: [s/n]: ')
    if continuar in 'sS':        
        continue
        os.system('clear')
    elif continuar in 'nN':
        print('FIM')
        
print()

for c in compra:
    for k, v in c.items():
        print(f'{k}: {v}')