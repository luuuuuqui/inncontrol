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
    def set_id_reserva(self, id_reserva: int) -> None: 
        if id_reserva <= 0: raise ValueError("ID da reserva deve ser um inteiro positivo.")
        self._id_reserva = id_reserva

    def set_id_hospede(self, id_hospede: int) -> None: 
        if id_hospede <= 0: raise ValueError("ID do hóspede deve ser um inteiro positivo.")
        self._id_hospede = id_hospede

    def set_id_quarto(self, id_quarto: int) -> None: 
        if id_quarto <= 0: raise ValueError("ID do quarto deve ser um inteiro positivo.")
        self._id_quarto = id_quarto

    def set_data_reserva(self, data_reserva: date) -> None: 
        if data_reserva < date.today(): raise ValueError("Data da reserva não pode ser no passado.")
        self._data_reserva = data_reserva

    def set_qtd_dias(self, qtd_dias: int) -> None: 
        if qtd_dias <= 0: raise ValueError("Quantidade de dias deve ser um inteiro positivo.")
        self._qtd_dias = qtd_dias

    def set_status(self, status: str) -> None: 
        if status == "": raise ValueError("Status da reserva não pode ser vazio.")
        self._status = status

    # Getters:
    def get_id_reserva(self) -> int: return self._id_reserva

    def get_id_hospede(self) -> int: return self._id_hospede

    def get_id_quarto(self) -> int: return self._id_quarto

    def get_data_reserva(self) -> date: return self._data_reserva

    def get_qtd_dias(self) -> int: return self._qtd_dias

    def get_status(self) -> str: return self._status

    # Métodos:
    def to_dict(self) -> dict:
        return {
            "id_reserva": self.get_id_reserva(),
            "id_hospede": self.get_id_hospede(),
            "id_quarto": self.get_id_quarto(),
            "data_reserva": self.get_data_reserva(),
            "qtd_dias": self.get_qtd_dias(),
            "status": self.get_status()
        }
    
    @staticmethod
    def from_row(row) -> 'Reserva':
        raise NotImplementedError("Método from_row ainda não implementado")

    def confirmar(self) -> None:
        pass

