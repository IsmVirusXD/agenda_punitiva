from datetime import datetime
'''
Objeto do Tipo Tareda, a ideia aqui é Objetificar as Tarefas para que
quando forem chamadas algumas funções mais simples sejam adquiridas
e Facilite a Vida do FrontEnd
'''


class Tarefa:
    # Inicializador
    def __init__(self, titulo: str, texto: str, year: str, month: str, day: str):
        self.titulo = titulo
        self.texto = texto
        self.date = datetime(int(year), int(month), int(day))

    # Getters
    def getTitulo(self) -> str:
        # Retorna o Titulo para o Prgrama
        texto = self.titulo
        return texto

    def getTexto(self) -> str:
        # Retorna o Texto para o Prgrama
        texto = self.texto
        return texto

    def getData(self) -> str:
        # Retorna a Data formatada para o Padrão
        date = self.date
        if date.day < 10:
            newdata = "0{} / {} / {}".format(date.day, date.month, date.year)
        else:
            newdata = "{} / {} / {}".format(date.day, date.month, date.year)
        return newdata

    # Functions:
    def day_Left(self) -> int:
        # Calcula o dia
        date = self.date.strftime("%j")
        today = datetime.now().strftime("%j")
        days_lefyt = int(date) - int(today)
        return days_lefyt

    def getSavedFile(self) -> str:
        # Configuta os arquivos para serem salvos em um formato especifico
        save = '{}|{}|{}|{}|{}'.format(
            self.date.day, self.date.month, self.date.year, self.titulo, self.texto)
        return save
