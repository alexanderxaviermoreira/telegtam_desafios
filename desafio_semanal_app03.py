import os


os.system('clear')

def cabecalho():
    os.system('clear')
    print('\n{:^40}'.format('#'*38))
    print('{:^40}'.format('#        agendador de tarefas        #').upper())
    print('{:^40}\n'.format('#'*38))

tarefas = []
dados_tarefa = {}
cabecalho()
qtde_tarefas = int(input('\nQUANTIDADE DE TAREFAS: '))
os.system('clear')
cabecalho()
for t in range(qtde_tarefas):
    dados_tarefa['Nome da Terefa'] = input('Nome da Terefa: ').upper()
    os.system('clear')
    cabecalho()
    dados_tarefa['Dia'] = int(input('Dia: '))
    os.system('clear')
    cabecalho()
    dados_tarefa['Mes'] = int(input('Mes: '))
    os.system('clear')
    cabecalho()
    dados_tarefa['Ano'] = int(input('Ano: '))
    os.system('clear')
    cabecalho()
    tarefas.append(dados_tarefa.copy())
    os.system('clear')
    cabecalho()

for r in tarefas:
    print()
    for k, v in r.items():
        print(f'{k}: {v}')
    
    

'''
Sistema de gerenciamento de tarefas

Fazer um programa que pergunte para o usuário quais tarefas ele irá realizar 
no dia , semana , mês essa parte fica a sua escolha quando o usuário tiver 
finalizado a sua tarefa ele terá que deletar essa tarefa do lugar na onde 
esta sendo armazenado suas informações (tarefas)

O programa teve responder da seguinte maneira 

Vc me passou as seguintes tarefas 

......
......
......
.....
.....

Esta correto se estiver tudo correto ele irá guardas essas informações 
caso alguma estiver errado o usuário poderá modificar apenas aquela 
que estiver errado 

Quando o usuário terminar a tarefa ele deverá excluir a tarefa já 
realizada e mostra a seguinte frase 

Vc já terminou a tarefa .....

Mas ainda falta as tarefas 

.....
.....
.....
.....

Quando o usuário finalizar todas as tarefas o programa deverá 
mostra algo parecido como 

Parabéns .... Por ter feito todas as suas tarefas
'''