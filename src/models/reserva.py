from datetime import date

class Reserva:
    def __init__(self, id_reserva: int,
     id_hospede: int, id_quarto: int, data_reserva: date, qtd_dias: int, status: str) -> None:
        self.set_id_reserva(id_reserva)
        self.set_id_hospede(id_hospede)
        self.set_id_quarto(id_quarto)
        self.set_data_reserva(data_reserva)
        self.set_qtd_dias(qtd_dias)
        self.set_status(status)

    # Setters:
    @staticmethod
    def set_id_reserva(self, id_reserva: int) -> None: self._id_reserva = id_reserva

    @staticmethod
    def set_id_hospede(self, id_hospede: int) -> None: self._id_hospede = id_hospede

    @staticmethod
    def set_id_quarto(self, id_quarto: int) -> None: self._id_quarto = id_quarto

    @staticmethod
    def set_data_reserva(self, data_reserva: date) -> None: self._data_reserva = data_reserva

    @staticmethod
    def set_qtd_dias(self, qtd_dias: int) -> None: self._qtd_dias = qtd_dias

    @staticmethod
    def set_status(self, status: str) -> None: self._status = status

    # Getters:
    @staticmethod
    def get_id_reserva(self) -> int: return self._id_reserva

    @staticmethod
    def get_id_hospede(self) -> int: return self._id_hospede

    @staticmethod
    def get_id_quarto(self) -> int: return self._id_quarto

    @staticmethod
    def get_data_reserva(self) -> date: return self._data_reserva

    @staticmethod
    def get_qtd_dias(self) -> int: return self._qtd_dias

    @staticmethod
    def get_status(self) -> str: return self._status

    # Métodos:
    @staticmethod
    def to_dict(self) -> dict:
        return {
            "id_reserva": self.get_id_reserva(),
            "id_hospede": self.get_id_hospede(),
            "id_quarto": self.get_id_quarto(),
            "data_reserva": self.get_data_reserva(),
            "qtd_dias": self.get_qtd_dias()
        }
    
    @staticmethod
    def from_row() -> None:
        pass

    @staticmethod
    def confirmar() -> None:
        pass

