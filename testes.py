from functions import *
from frontend import *
from obj_tarefa import Tarefa
from obj_punicoes import Punicioes

tarefas = loadList()
punicoes = loadPunicoes()

print(random_punicao(punicoes))