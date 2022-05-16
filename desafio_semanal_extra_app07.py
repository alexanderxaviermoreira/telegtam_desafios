import os

produtos = [
    {'id': 100, 'descricao': 'cachorro quente', 'valor': 9.00, },
    {'id': 101, 'descricao': 'cachorro quente duplo', 'valor': 11.00, },
    {'id': 102, 'descricao': 'x-egg', 'valor': 12.00, },
    {'id': 103, 'descricao': 'x-salada', 'valor': 13.00, },
    {'id': 104, 'descricao': 'x-bacon', 'valor': 14.00, },
    {'id': 105, 'descricao': 'x-tudo', 'valor': 17.00, },
    {'id': 200, 'descricao': 'refrigerante lata', 'valor': 5.00, },
    {'id': 201, 'descricao': 'cha gelado', 'valor': 4.00, },
]
dados = {}
compra = []
os.system('clear')

codigo = int(input('Código: '))
for e, c in enumerate(produtos):
    for k, v in c.items():
        if codigo == v:
            continuar = input('Deseja continuar [s/n]: ')
            print(f"Você pediu {produtos['descricao']} no valor de {produtos['valor']}")