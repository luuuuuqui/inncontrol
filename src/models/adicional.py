from decimal import Decimal, ROUND_HALF_UP


class Adicional:
    def __init__(
        self, id_adicional: int, descricao: str, valor: Decimal | str | float
    ) -> None:
        self.set_id_adicional(id_adicional)
        self.set_descricao(descricao)
        self.set_valor(valor)

    def set_id_adicional(self, id_adicional: int):
        if id_adicional < 0:
            raise ValueError("ID do adicional deve ser um inteiro positivo.")
        self.__id_adicional = id_adicional

    def set_descricao(self, descricao: str) -> None:
        if not descricao.strip():
            raise ValueError("Descrição do adicional não pode ser vazia.")
        self.__descricao = descricao

    def set_valor(self, valor: Decimal | str | float) -> None:
        if isinstance(valor, float):
            valor = str(valor)

        if isinstance(valor, str):
            valor = valor.strip()
            valor = valor.replace(",", ".")

        if not isinstance(valor, Decimal):
            try:
                valor = Decimal(valor)
            except Exception:
                raise ValueError(f"Valor inválido: {valor}")

        if valor < 0:
            raise ValueError("Valor do adicional não pode ser negativo.")

        self.__valor = valor.quantize(Decimal("0.00"), rounding=ROUND_HALF_UP)

    def get_id_adicional(self) -> int:
        return self.__id_adicional

    def get_descricao(self) -> str:
        return self.__descricao

    def get_valor(self) -> str:
        return str(self.__valor)

    def to_dict(self) -> dict:
        return {
            "id_adicional": self.get_id_adicional(),
            "descricao": self.get_descricao(),
            "valor": str(self.get_valor()),
        }

    def __str__(self) -> str:
        return (
            f"{self.get_id_adicional()} - {self.get_descricao()} - {self.get_valor()}"
        )
