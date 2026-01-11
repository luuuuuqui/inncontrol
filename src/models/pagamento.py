from datetime import date
from decimal import Decimal, ROUND_HALF_UP


class Pagamento:
    def __init__(
        self,
        id_pagamento: int,
        id_reserva: int,
        data_pagamento: date,
        valor_total: Decimal | str | float,
        forma_pagamento: str,
        status: str,
    ) -> None:
        self.set_id_pagamento(id_pagamento)
        self.set_id_reserva(id_reserva)
        self.set_data_pagamento(data_pagamento)
        self.set_valor_total(valor_total)
        self.set_forma_pagamento(forma_pagamento)
        self.set_status(status)

    # Setters:
    def set_id_pagamento(self, id_pagamento: int) -> None:
        if id_pagamento <= 0:
            raise ValueError("ID do pagamento deve ser um inteiro positivo.")
        self._id_pagamento = id_pagamento

    def set_id_reserva(self, id_reserva: int) -> None:
        if id_reserva <= 0:
            raise ValueError("ID da reserva deve ser um inteiro positivo.")
        self._id_reserva = id_reserva

    def set_data_pagamento(self, data_pagamento: date) -> None:
        if data_pagamento > date.today():
            raise ValueError("Data do pagamento não pode ser no futuro.")
        self._data_pagamento = data_pagamento

    def set_valor_total(self, valor_total: Decimal | str | float) -> None:
        if isinstance(valor_total, str):
            try:
                valor_total = Decimal(valor_total)
            except (ValueError, TypeError):
                raise ValueError("Valor total do pagamento inválido.")
        elif isinstance(valor_total, float):
            try:
                valor_total = Decimal(str(valor_total)).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
            except (ValueError, TypeError):
                raise ValueError("Valor total do pagamento inválido.")
        elif not isinstance(valor_total, Decimal):
            raise ValueError("Valor total do pagamento deve ser Decimal, str ou float.")
        
        if valor_total < 0: # pyright: ignore[reportOperatorIssue]
            raise ValueError("Valor total do pagamento não pode ser negativo.")
        self._valor_total = valor_total

    def set_forma_pagamento(self, forma_pagamento: str) -> None:
        if forma_pagamento == "":
            raise ValueError("Forma de pagamento não pode ser vazia.")
        self._forma_pagamento = forma_pagamento

    def set_status(self, status: str) -> None:
        if status == "":
            raise ValueError("Status do pagamento não pode ser vazio.")
        self._status = status

    # Getters:
    def get_id_pagamento(self) -> int:
        return self._id_pagamento

    def get_id_reserva(self) -> int:
        return self._id_reserva

    def get_data_pagamento(self) -> date:
        return self._data_pagamento

    def get_valor_total(self) -> Decimal:
        return self._valor_total

    def get_forma_pagamento(self) -> str:
        return self._forma_pagamento

    def get_status(self) -> str:
        return self._status

    # Métodos:
    def to_dict(self) -> dict:
        return {
            "id_pagamento": self.get_id_pagamento(),
            "id_reserva": self.get_id_reserva(),
            "data_pagamento": self.get_data_pagamento(),
            "valor_total": self.get_valor_total(),
            "forma_pagamento": self.get_forma_pagamento(),
            "status": self.get_status(),
        }
    
    def __str__(self) -> str:
        return (
            f"{self.get_id_pagamento()} - {self.get_id_reserva()} - {self.get_data_pagamento()} - {self.get_valor_total()} - {self.get_forma_pagamento()} - {self.get_status()}"
        )
