from os import system
from functions import random_punicao
from obj_tarefa import Tarefa
from obj_punicoes import Punicioes


def menu() -> int:
    system('cls')

    print('- - - - - - - - - - - - - - - - -')
    print('|Menu:                          |')
    print('- - - - - - - - - - - - - - - - -')
    print('| 1 | Visualizar Tarefa de Hoje |')
    print('| 2 | Adicionar Tarefa          |')
    print('| 3 | Adicionar Punicao         |')
    print('| 4 | Remover Tarefa            |')
    print('| 5 | Remover Punicao           |')
    print('| 6 | Sair                      |')
    print('- - - - - - - - - - - - - - - - -')
    valor = int(input('Opção:    '))

    return valor


def telaView(lista: [Tarefa], punicao: [Punicioes]):
    system('cls')
    index = 0
    print('===========================================================================================================================================================================================================')
    print('|Tarefas:                                                                                                                                                                                                 |')
    print('===========================================================================================================================================================================================================')
    for i in lista:
        if i.day_Left() == 0:
            index = index + 1
            print('|{}| + {}: {}'.format(index,
                  i.getTitulo(), i.getTexto()).strip())
            print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')

        elif i.day_Left() > 0:
            index = index + 1
            print('|{}| + {}: {}'.format(index,
                  i.getTitulo(), i.getTexto()).strip())
            print('--> Punição: {}'.format(random_punicao(punicao).strip()))
            print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')


def telaAllView(lista: [Tarefa]):
    index = 0
    print('===========================================================================================================================================================================================================')
    print('Todas as Tarefas                                                                                                                                                                                              |')
    print('===========================================================================================================================================================================================================')
    for i in lista:
        index = index + 1
        print('|{}| {} | {}: {} [Falta: {} dias]'.format(
            index, i.getData(), i.getTitulo(), i.getTexto().strip(), i.day_Left()))
        print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')


def telaAllPunicoes(lista: [Punicioes]):
    index = 0
    print('===========================================================================================================================================================================================================')
    print('Todas as Punicoes                                                                                                                                                                                            |')
    print('===========================================================================================================================================================================================================')
    for i in lista:
        index = index + 1
        print('|{}| {} : {}'.format(index, i.getTitulo(), i.getPunicoes().strip()))
        print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')
