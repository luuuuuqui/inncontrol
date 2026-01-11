from datetime import datetime, timedelta


class Reserva:
    def __init__(
        self,
        id_reserva: int,
        id_hospede: int,
        id_quarto: int,
        data_reserva: datetime | str,
        qtd_dias: int | timedelta,
        status: str,
    ) -> None:
        self.set_id_reserva(id_reserva)
        self.set_id_hospede(id_hospede)
        self.set_id_quarto(id_quarto)
        self.set_data_reserva(data_reserva)
        self.set_qtd_dias(qtd_dias)
        self.set_status(status)

    # Setters:
    def set_id_reserva(self, id_reserva: int) -> None:
        if id_reserva < 0:
            raise ValueError("ID da reserva deve ser um inteiro positivo.")
        self.__id_reserva = id_reserva

    def set_id_hospede(self, id_hospede: int) -> None:
        if id_hospede < 0:
            raise ValueError("ID do hóspede deve ser um inteiro positivo.")
        self.__id_hospede = id_hospede

    def set_id_quarto(self, id_quarto: int) -> None:
        if id_quarto < 0:
            raise ValueError("ID do quarto deve ser um inteiro positivo.")
        self.__id_quarto = id_quarto

    def set_data_reserva(self, data_reserva: datetime | str) -> None:
        if isinstance(data_reserva, str):
            try:
                data_reserva = datetime.strptime(data_reserva, "%Y-%m-%d")
            except ValueError:
                raise ValueError("Data de reserva inválida.")
        elif not isinstance(data_reserva, datetime):
            raise ValueError("Data de reserva inválida.")

        if data_reserva < datetime.today():
            raise ValueError("Data da reserva não pode ser no passado.")
        self.__data_reserva = data_reserva

    def set_qtd_dias(self, qtd_dias: int | timedelta) -> None:
        if isinstance(qtd_dias, timedelta):
            qtd_dias = qtd_dias.days
        elif not isinstance(qtd_dias, int):
            raise ValueError("Quantidade de dias deve ser um inteiro ou timedelta.")

        if qtd_dias <= 0:
            raise ValueError("Quantidade de dias deve ser um inteiro positivo.")

        self.__qtd_dias = qtd_dias

    def set_status(self, status: str) -> None:
        if status == "":
            raise ValueError("Status da reserva não pode ser vazio.")
        self.__status = status

    # Getters:
    def get_id_reserva(self) -> int:
        return self.__id_reserva

    def get_id_hospede(self) -> int:
        return self.__id_hospede

    def get_id_quarto(self) -> int:
        return self.__id_quarto

    def get_data_reserva(self) -> datetime:
        return datetime.strftime(self.__data_reserva, "%Y-%m-%d") # pyright: ignore[reportReturnType]

    def get_qtd_dias(self) -> int:
        return self.__qtd_dias

    def get_status(self) -> str:
        return self.__status

    # Métodos:
    def to_dict(self) -> dict:
        return {
            "id_reserva": self.get_id_reserva(),
            "id_hospede": self.get_id_hospede(),
            "id_quarto": self.get_id_quarto(),
            "data_reserva": self.get_data_reserva(),
            "qtd_dias": self.get_qtd_dias(),
            "status": self.get_status(),
        }
