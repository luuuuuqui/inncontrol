from decimal import Decimal, ROUND_HALF_UP


class TipoQuarto:
    def __init__(
        self,
        id_tipoquarto: int,
        nome: str,
        descricao: str,
        capacidade: int,
        valor_diaria: Decimal,
    ) -> None:
        self.set_id_tipoquarto(id_tipoquarto)
        self.set_nome(nome)
        self.set_descricao(descricao)
        self.set_capacidade(capacidade)
        self.set_valor_diaria(valor_diaria)

    def set_id_tipoquarto(self, id: int) -> None:
        if id < 0:
            raise ValueError("ID do tipo de quarto deve ser um inteiro positivo.")
        self.__id_tipoquarto = id

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

    def set_valor_diaria(self, valor_diaria: Decimal) -> None:
        if isinstance(valor_diaria, float):
            valor_diaria = str(valor_diaria)

        if isinstance(valor_diaria, str):
            valor_diaria = valor_diaria.strip()
            valor_diaria = valor_diaria.replace(',', '.')
        
        if not isinstance(valor_diaria, Decimal):
            try:
                valor_diaria = Decimal(valor_diaria)
            except Exception:
                raise ValueError(f"Valor inválido: {valor_diaria}")

        if valor_diaria < 0:
            raise ValueError("Valor do adicional não pode ser negativo.")
        
        self.__valor_diaria = valor_diaria.quantize(Decimal("0.00"), rounding=ROUND_HALF_UP)

    def get_id_tipoquarto(self) -> int:
        return self.__id_tipoquarto

    def get_nome(self) -> str:
        return self.__nome

    def get_descricao(self) -> str:
        return self.__descricao

    def get_capacidade(self) -> int:
        return self.__capacidade

    def get_valor_diaria(self) -> str:
        return str(self.__valor_diaria)

    def to_dict(self) -> dict:
        return {
            "id_tipoquarto": self.get_id_tipoquarto(),
            "nome": self.get_nome(),
            "descricao": self.get_descricao(),
            "capacidade": self.get_capacidade(),
            "valor_diaria": str(self.get_valor_diaria()),
        }

    def __str__(self) -> str:
        return f"{self.get_id_tipoquarto()} - {self.get_nome()}"
