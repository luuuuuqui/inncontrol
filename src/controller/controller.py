from models.teste import Teste, TesteDAO

class Controller:
    # Itens 
    @staticmethod
    def teste_inserir(nome):
        teste = Teste(0, nome)
        TesteDAO.inserir(teste)

    @staticmethod
    def teste_listar():
        return TesteDAO.listar()

    @staticmethod
    def teste_listar_id(id):
        return TesteDAO.listar_id(id)

    @staticmethod
    def teste_atualizar(id, nome):
        teste = Teste(id, nome)
        TesteDAO.atualizar(teste)

    @staticmethod
    def teste_excluir(id):
        TesteDAO.excluir(id)