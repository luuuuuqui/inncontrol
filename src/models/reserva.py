from datetime import datetime


class Reserva:
    def __init__(
        self,
        id_reserva: int,
        id_hospede: int,
        id_quarto: int,
        data_checkin: datetime | str,
        data_checkout: datetime | str,
        status: str
    ) -> None:
        self.set_id_reserva(id_reserva)
        self.set_id_hospede(id_hospede)
        self.set_id_quarto(id_quarto)
        self.set_data_checkin(data_checkin)
        self.set_data_checkout(data_checkout)
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

    def set_data_checkin(self, data_checkin: datetime | str) -> None:
        if isinstance(data_checkin, str):
            try:
                data_checkin = datetime.strptime(data_checkin, "%Y-%m-%d")
            except ValueError as e:
                raise ValueError(f"Data de Check-In inválida. {e}")

        if data_checkin < datetime.strptime("2026-01-01", "%Y-%m-%d"):
            raise ValueError("Data de Check-In não pode ser antes de 2026.")
        self.__data_checkin = data_checkin

    def set_data_checkout(self, data_checkout: datetime | str) -> None:
        if isinstance(data_checkout, str):
            try:
                data_checkout = datetime.strptime(data_checkout, "%Y-%m-%d")
            except ValueError as e:
                raise ValueError(f"Data de Check-Out inválida. {e}")

        if data_checkout < datetime.strptime("2026-01-01", "%Y-%m-%d"):
            raise ValueError("Data de Check-Out não pode ser antes de 2026.")
        
        if self.__data_checkin and data_checkout <= self.__data_checkin:
            raise ValueError("A data de check-out não pode ser antes da data de check-in.")
    
        self.__data_checkout = data_checkout
        

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

    def get_data_checkin(self) -> str:
        return datetime.strftime(self.__data_checkin, "%Y-%m-%d")

    def get_data_checkout(self) -> str:
        return datetime.strftime(self.__data_checkout, "%Y-%m-%d")

    def get_status(self) -> str:
        return self.__status

    # Métodos:
    def to_dict(self) -> dict:
        return {
            "id_reserva": self.get_id_reserva(),
            "id_hospede": self.get_id_hospede(),
            "id_quarto": self.get_id_quarto(),
            "data_checkin": self.get_data_checkin(),
            "data_checkout": self.get_data_checkout(),
            "status": self.get_status(),
        }
