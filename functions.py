import random
from obj_tarefa import Tarefa
from obj_punicoes import Punicioes


'''
Aqui estão todas as Funções que são usadas no Programa para qualquer 
tipo de tratamento que sera repetido varias e varias vezes.
Organizado por ordem Alfabetica
'''


def adicionar() -> Tarefa:
    # Cadastra uma Tarefa
    titulo = input("Titulo: ")

    texto = input("Descrição: ")

    day = int(input("Dia: "))
    month = int(input("Mes: "))
    year = int(input("Ano: "))

    arquivo = Tarefa(titulo, texto, year, month, day)
    return arquivo


def converting(content: str) -> Tarefa:
    # Converte str para o tipo: Tarefa
    arquivo = content.split("|")
    day = arquivo[0]
    month = arquivo[1]
    year = arquivo[2]

    titulo = arquivo[3]

    texto = arquivo[4]

    new = Tarefa(titulo, texto, year, month, day)
    return new


def con_Punicoes(content: str) -> Punicioes:
    arquivo = content.split("|")
    titulo = arquivo[0]
    texto = arquivo[1]

    new = Punicioes(titulo, texto)
    return new


def loadList() -> [Tarefa]:
    # Carrega todos os dados do txt
    f_contents = []
    lista = []
    with open('savedata.txt', 'r') as f:
        f_contents = f.readlines()
        for i in f_contents:
            lista.append(converting(i))
    return lista


def loadPunicoes() -> [Tarefa]:
    # Carrega todos os dados do txt
    f_contents = []
    lista = []
    with open('punicao.txt', 'r') as f:
        f_contents = f.readlines()
        for i in f_contents:
            lista.append(con_Punicoes(i))
    return lista


def remover(lista: [], index: int):
    # Remove uma Tarefa
    index = index - 1
    lista.pop(index)


def saveList(tobesave=[Tarefa]):
    # Salva os Dados dentro de um .txt
    with open('savedata.txt', 'w') as f:
        for line in tobesave:
            f.write(line.getSavedFile())


def savePunicoes(tobesave=[Tarefa]):
    # Salva os Dados dentro de um .txt
    with open('punicao.txt', 'w') as f:
        for line in tobesave:
            f.write(line.getSavedFile())

def add_punicoes() -> Punicioes:

    titulo = input("Titulo da Puniçães: ")
    texto = input("Descrição: ")

    arquivo = Punicioes(titulo, texto)
    return arquivo


def random_punicao(punicao: [Punicioes]) -> str:
    tamanho = len(punicao)
    index = random.randrange(0, tamanho)
    return punicao[index].getPunicoes()
