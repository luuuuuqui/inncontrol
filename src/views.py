from dao.testedao import TesteDAO
from models.teste import Teste

class View:
    # Itens 
    @staticmethod
    def teste_inserir(nome):
        teste = Teste(0, nome)
        TesteDAO.inserir(teste)

    @staticmethod
    def teste_listar():
        r = TesteDAO.listar()
        r.sort(key = lambda obj : obj.get_name())            
        return r

    @staticmethod
    def teste_listar_id(id):
        return TesteDAO.listar_id(id)

    @staticmethod
    def teste_atualizar(id, nome):
        teste = Teste(id, nome)
        TesteDAO.atualizar(teste)

    @staticmethod
    def teste_excluir(id: int):
        teste = Teste(id, "")
        TesteDAO.excluir(teste)