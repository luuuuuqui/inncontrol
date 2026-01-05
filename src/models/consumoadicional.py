from datetime import datetime


class ConsumoAdicional:
    def __init__(
        self,
        id_consumo: int,
        id_reserva: int,
        id_adicional: int,
        quantidade: int,
        data_consumo: datetime,
    ) -> None:
        self.set_id_consumo(id_consumo)
        self.set_id_reserva(id_reserva)
        self.set_id_adicional(id_adicional)
        self.set_quantidade(quantidade)
        self.set_data_consumo(data_consumo)

    # Setters:
    def set_id_consumo(self, id_consumo: int) -> None:
        if id_consumo <= 0:
            raise ValueError("ID do consumo deve ser um inteiro positivo.")
        self._id_consumo = id_consumo

    def set_id_reserva(self, id_reserva: int) -> None:
        if id_reserva <= 0:
            raise ValueError("ID da reserva deve ser um inteiro positivo.")
        self._id_reserva = id_reserva

    def set_id_adicional(self, id_adicional: int) -> None:
        if id_adicional <= 0:
            raise ValueError("ID do adicional deve ser um inteiro positivo.")
        self._id_adicional = id_adicional

    def set_quantidade(self, quantidade: int) -> None:
        if quantidade < 0:
            raise ValueError("Quantidade do consumo não pode ser negativa.")
        self._quantidade = quantidade

    def set_data_consumo(self, data_consumo: datetime) -> None:
        if data_consumo > datetime.now():
            raise ValueError("Data do consumo não pode ser no futuro.")
        self._data_consumo = data_consumo

    # Getters:
    def get_id_consumo(self) -> int:
        return self._id_consumo

    def get_id_reserva(self) -> int:
        return self._id_reserva

    def get_id_adicional(self) -> int:
        return self._id_adicional

    def get_quantidade(self) -> int:
        return self._quantidade

    def get_data_consumo(self) -> datetime:
        return self._data_consumo

    # Métodos:
    def to_dict(self) -> dict:
        return {
            "id_consumo": self.get_id_consumo(),
            "id_reserva": self.get_id_reserva(),
            "id_adicional": self.get_id_adicional(),
            "quantidade": self.get_quantidade(),
            "data_consumo": self.get_data_consumo(),
        }