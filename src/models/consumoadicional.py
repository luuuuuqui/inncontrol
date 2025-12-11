from datetime import datetime

class ConsumoAdicional:
    def __init__(self, id_consumo: int, id_reserva: int, id_adicional: int, quantidade: int, data_consumo: datetime) -> None:
        self.set_id_consumo(id_consumo)
        self.set_id_reserva(id_reserva)
        self.set_id_adicional(id_adicional)
        self.set_quantidade(quantidade)
        self.set_data_consumo(data_consumo)

    # Setters:
    @staticmethod
    def set_id_consumo(self, id_consumo: int) -> None: self._id_consumo = id_consumo

    @staticmethod
    def set_id_reserva(self, id_reserva: int) -> None: self._id_reserva = id_reserva

    @staticmethod
    def set_id_adicional(self, id_adicional: int) -> None: self._id_adicional = id_adicional

    @staticmethod
    def set_quantidade(self, quantidade: int) -> None: self._quantidade = quantidade

    @staticmethod
    def set_data_consumo(self, data_consumo: datetime) -> None: self._data_consumo = data_consumo

    # Getters:
    @staticmethod
    def get_id_consumo(self) -> int: return self._id_consumo

    @staticmethod
    def get_id_reserva(self) -> int: return self._id_reserva

    @staticmethod
    def get_id_adicional(self) -> int: return self._id_adicional

    @staticmethod
    def get_quantidade(self) -> int: return self._quantidade

    @staticmethod
    def get_data_consumo(self) -> datetime: return self._data_consumo

    # Métodos:
    @staticmethod
    def to_dict(self) -> dict:
        return {
            "id_consumo": self.get_id_consumo(),
            "id_reserva": self.get_id_reserva(),
            "id_adicional": self.get_id_adicional(),
            "quantidade": self.get_quantidade(),
            "data_consumo": self.get_data_consumo()
        }
    
    @staticmethod
    def from_row() -> None:
        pass