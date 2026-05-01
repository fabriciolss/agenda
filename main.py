def menu() -> str:
    return("Menu do Gerenciador de Lista de Tarefas: \n"
          "1. Adicionar Tarefa\n"
          "2. Ver Tarefa\n"
          "3. Atualizar Tarefa\n"
          "4. Completar Tarefa\n"
          "5. Deletar Tarefas Completadas\n"
          "6. Sair")

class Tarefas:
    def __init__(self):
        self.tarefas = []

    def menu(self) -> str:
        return ("Menu do Gerenciador de Lista de Tarefas: \n"
          "1. Adicionar Tarefa\n"
          "2. Ver Tarefa\n"
          "3. Atualizar Tarefa\n"
          "4. Completar Tarefa\n"
          "5. Deletar Tarefa\n"
          "6. Deletar Tarefas Completadas\n"
          "7. Sair\n")

    def adicionartarefa(self, descricao: str):
        id = len(self.tarefas) + 1
        self.tarefas.append({"id": id, "descricao": descricao, "completada": False})

    def vertarefa(self):
        for tarefa in self.tarefas:
            check = "[ ✓ ] " if tarefa["completada"] else "[ ]"
            print(f'{tarefa["id"]}. {check} {tarefa["descricao"]}\n')

    def atualizartarefa(self, id: int, descricao: str):
        for tarefa in self.tarefas:
            if tarefa["id"] == id:
                self.tarefas[tarefa["id"] - 1]["descricao"] = descricao

    def completartarefa(self, id: int):
        for tarefa in self.tarefas:
            if tarefa["id"] == id:
                self.tarefas[tarefa["id"] - 1]["completada"] = True

    def deletartarefa(self, id: int):
        for tarefa in self.tarefas:
            if tarefa["id"] == id:
                self.tarefas.remove(tarefa)

        self.atualizarindices()

    def atualizarindices(self):
        ordenador = 1
        for tarefa in self.tarefas:
            self.tarefas[ordenador-1]["id"] = ordenador
            ordenador += 1

    def deletartarefascompletadas(self):
        for tarefa in self.tarefas:
            if tarefa["completada"]:
                self.tarefas.remove(tarefa)

        self.atualizarindices()

menutarefas = True
Tarefas = Tarefas()

while menutarefas:
    print(Tarefas.menu())
    escolha = int(input("Digite sua escolha:"))

    if escolha == 1:
        tarefa = input("Digite o nome do tarefa: ")
        Tarefas.adicionartarefa(tarefa)
    elif escolha == 2:
        Tarefas.vertarefa()
    elif escolha == 3:
        Tarefas.vertarefa()
        idtarefa = int(input("Digite o número da tarefa a ser atualizada: "))
        novadescricao = input("Digite o novo nome da tarefa: ")
        Tarefas.atualizartarefa(idtarefa, novadescricao)
    elif escolha == 4:
        idtarefa = int(input("Digite o número da tarefa a ser completada: "))
        Tarefas.completartarefa(idtarefa)
    elif escolha == 5:
        idtarefa = int(input("Digite o número da tarefa a ser removida: "))
        Tarefas.deletartarefa(idtarefa)
    elif escolha == 6:
        Tarefas.deletartarefascompletadas()
    elif escolha == 7:
        menutarefas = False
