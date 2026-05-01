class Agenda:
    def __init__(self):
        self.agenda = []

    def menu(self):
        print("Selecione uma das opções abaixo:\n"
              "1. Adicionar contato\n"
              "2. Editar contato\n"
              "3. Listar contatos\n"
              "4. Listar contatos favoritos\n"
              "5. Favoritar contato\n"
              "6. Deletar contato\n"
              "7. Sair\n")

    def adicionarcontato(self, nome: str, telefone: str, email: str):
        contato = {'id': len(self.agenda) + 1, 'nome': nome, 'telefone': telefone, 'email': email, "favorito": False}
        self.agenda.append(contato)

    def listarcontatos(self):
        for contato in self.agenda:
            print(f'{contato['id']}. Nome do contato: {contato["nome"]}, telefone: {contato["telefone"]}, '
                  f'email: {contato["email"]}, favorito:{'SIM'if contato["favorito"] else 'NÃO'}\n')

    def editarcontato(self):
        try:
            selecao = self.selecao()
            alterar = input('Digite o item a ser alterado')
            valor = input('Digite o novo valor do contato')

            if alterar.lower() in ['nome', 'telefone', 'email']:
                self.agenda[selecao - 1][alterar] = valor
        except ValueError as e:
            print(f'Informação inválida. Tente novamente {e.__cause__}')
        except IndexError as e:
            print(f'ID inválido. Tente novamente.')

    def favoritar(self):
        selecao = self.selecao()
        try:
            self.agenda[selecao-1]['favorito'] = not self.agenda[selecao-1]['favorito']
        except ValueError:
            print('Digite um número válido. Tente novamente')

    def listarcontatosfavoritos(self):
        for contato in self.agenda:
            if contato['favorito']:
                print(f'{contato['id']}. Nome do contato: {contato["nome"]}, telefone: {contato["telefone"]}, email: {contato["email"]}\n')
            
    def deletarcontato(self):
        selecao = self.selecao()
        for contato in self.agenda:
            if contato['id'] == selecao:
                self.agenda.remove(contato)

    def selecao(self) -> int:
        self.listarcontatos()
        return int(input('Selecione o contato a ser alterado digitando o número de id'))

menu_agenda = True
agenda = Agenda()

while menu_agenda:
    agenda.menu()
    opcao = int(input('Digite o número de uma das opções disponíveis'))

    if opcao == 1:
        agenda.adicionarcontato(nome=str(input('Digite o nome do contato')),
                                telefone=str(input('Digite o telefone do contato')),
                                email=str(input('Digite o email do contato')))
    elif opcao == 2:
        agenda.editarcontato()
    elif opcao == 3:
        agenda.listarcontatos()
    elif opcao == 4:
        agenda.listarcontatosfavoritos()
    elif opcao == 5:
        agenda.favoritar()
    elif opcao == 6:
        agenda.deletarcontato()
    elif opcao == 7:
        menu_agenda = False
    else:
        print('Opção inválida. Tente novamente')
