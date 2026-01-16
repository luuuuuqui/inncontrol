from datetime import date, datetime
from decimal import Decimal, ROUND_HALF_UP


class Pagamento:
    def __init__(
        self,
        id_pagamento: int,
        id_reserva: int,
        data_pagamento: date | str,
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
    def set_id_pagamento(self, id: int) -> None:
        if id < 0:
            raise ValueError("ID do pagamento deve ser um inteiro positivo.")
        self.__id_pagamento = id

    def set_id_reserva(self, id: int) -> None:
        if id <= 0:
            raise ValueError("ID da reserva deve ser um inteiro positivo.")
        self.__id_reserva = id

    def set_data_pagamento(self, data_pagamento: date | str) -> None:
        if isinstance(data_pagamento, str):
            try:
                data_obj = datetime.strptime(data_pagamento, "%Y-%m-%d").date()
                data_pagamento = data_obj
            except ValueError:
                raise ValueError(
                    "Data do pagamento deve estar no formato 'YYYY-MM-DD'."
                )
        elif not isinstance(data_pagamento, date):
            raise TypeError("Data do pagamento deve ser um objeto date ou uma string.")

        if data_pagamento > date.today():
            raise ValueError("Data do pagamento não pode ser no futuro.")

        self.__data_pagamento = data_pagamento

    def set_valor_total(self, valor_total: Decimal | str | float) -> None:
        if isinstance(valor_total, float):
            valor_total = str(valor_total)

        if isinstance(valor_total, str):
            valor_total = valor_total.strip().replace(",", ".")

        if not isinstance(valor_total, Decimal):
            try:
                valor_total = Decimal(valor_total)
            except Exception:
                raise ValueError(f"Valor total inválido: {valor_total}")

        if valor_total < 0:
            raise ValueError("Valor total do pagamento não pode ser negativo.")

        self.__valor_total = valor_total.quantize(
            Decimal("0.01"), rounding=ROUND_HALF_UP
        )

    def set_forma_pagamento(self, forma_pagamento: str) -> None:
        if not forma_pagamento or forma_pagamento.strip() == "":
            raise ValueError("Forma de pagamento não pode ser vazia.")
        self.__forma_pagamento = forma_pagamento.strip()

    def set_status(self, status: str) -> None:
        if not status or status.strip() == "":
            raise ValueError("Status do pagamento não pode ser vazio.")
        self.__status = status.strip()

    # Getters:
    def get_id_pagamento(self) -> int:
        return self.__id_pagamento

    def get_id_reserva(self) -> int:
        return self.__id_reserva

    def get_data_pagamento(self) -> str:
        return self.__data_pagamento.strftime("%Y-%m-%d")

    def get_valor_total(self) -> str:
        return str(self.__valor_total)

    def get_forma_pagamento(self) -> str:
        return self.__forma_pagamento

    def get_status(self) -> str:
        return self.__status

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
            f"{self.get_id_pagamento()} - "
            f"{self.get_id_reserva()} - "
            f"{self.get_data_pagamento()} - "
            f"{self.get_valor_total()} - "
            f"{self.get_forma_pagamento()} - "
            f"{self.get_status()}"
        )
