from decimal import Decimal as decimal


class TipoQuarto:
    def __init__(
        self,
        id: int,
        nome: str,
        descricao: str,
        capacidade: int,
        valor_diaria: decimal,
    ) -> None:
        self.set_id(id)
        self.set_nome(nome)
        self.set_descricao(descricao)
        self.set_capacidade(capacidade)
        self.set_valor_diaria(valor_diaria)

    # Setters:
    def set_id(self, id: int) -> None:
        if id < 0:
            raise ValueError("ID do tipo de quarto deve ser um inteiro positivo.")
        self.__id = id

    def set_nome(self, nome: str) -> None:
        if nome == "".strip():
            raise ValueError("Nome do tipo de quarto não pode ser vazio.")
        self.__nome = nome

    def set_descricao(self, descricao: str) -> None:
        if descricao == "".strip():
            raise ValueError("Descrição do tipo de quarto não pode ser vazia.")
        self.__descricao = descricao

    def set_capacidade(self, capacidade: int) -> None:
        if capacidade <= 0:
            raise ValueError(
                "Capacidade do tipo de quarto deve ser um inteiro positivo."
            )
        self.__capacidade = capacidade

    def set_valor_diaria(self, valor_diaria: decimal) -> None:
        if valor_diaria <= 0:
            raise ValueError("Valor da diária não pode ser negativo ou zero.")
        self.__valor_diaria = valor_diaria

    # Getters:
    def get_id(self) -> int:
        return self.__id

    def get_nome(self) -> str:
        return self.__nome

    def get_descricao(self) -> str:
        return self.__descricao

    def get_capacidade(self) -> int:
        return self.__capacidade

    def get_valor_diaria(self) -> decimal:
        return self.__valor_diaria

    # Métodos:
    def to_dict(self) -> dict:
        return {
            "id": self.get_id(),
            "nome": self.get_nome(),
            "descricao": self.get_descricao(),
            "capacidade": self.get_capacidade(),
            "valor_diaria": self.get_valor_diaria(),
        }