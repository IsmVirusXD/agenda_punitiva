from os import system
from frontend import *
from functions import *
from obj_tarefa import Tarefa
from obj_punicoes import Punicioes

if __name__ == '__main__':
    key = 1
    tarefas = loadList()
    punicoes = loadPunicoes()

    while key:
        decisao = menu()

        # Vizualizar Tarefa de Hoje
        if decisao == 1:
            telaView(tarefas, punicoes)
            input()

        # Adicionar uma Tarefa
        if decisao == 2:
            system('cls')
            tarefas.append(adicionar())
            saveList(tarefas)

        # Adicionar uma Tarefa
        if decisao == 2:
            system('cls')
            tarefas.append(adicionar())
            saveList(tarefas)

        # Adicionar uma Punicao
        if decisao == 3:
            system('cls')
            punicoes.append(add_punicoes())
            savePunicoes(punicoes)

        # Remover uma Tarefa
        if decisao == 4:
            system('cls')
            telaAllView(tarefas)
            valor = input('|Digite o numero da Tarefa [0 - Cancela]: ')
            if valor != '0':
                remover(tarefas, int(valor))
                saveList(tarefas)

        # Remover uma Punicoes
        if decisao == 5:
            system('cls')
            telaAllPunicoes(punicoes)
            valor = input('|Digite o numero da Punicao [0 - Cancela]: ')
            if valor != '0':
                remover(punicoes, int(valor))
                savePunicoes(punicoes)

        # Sair do Programa
        if decisao == 6:
            system('cls')
            print("| Bye Bye | xD |")
            key = 0
