'''
Objeto do Tipo Tareda, a ideia aqui é Objetificar as Tarefas para que
quando forem chamadas algumas funções mais simples sejam adquiridas
e Facilite a Vida do FrontEnd
'''


class Punicioes:
    # Inicializador:
    def __init__(self, titulo: str, texto: str):
        self.titulo = titulo
        self.texto = texto

    # Getters
    def getPunicoes(self) -> str:
        texto = self.texto
        return texto

    def getTitulo(self) -> str:
        titulo = self.titulo
        return titulo

    # Functions:
    def getSavedFile(self) -> str:
        # Configuta os arquivos para serem salvos em um formato especifico
        save = '{}|{}'.format(self.titulo, self.texto)
        return save
