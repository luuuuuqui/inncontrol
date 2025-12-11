from datetime import date 
from decimal import Decimal as decimal

class Pagamento:
    def __init__(self, id_pagamento: int, id_reserva: int, data_pagamento: date, valor_total: float, forma_pagamento: str, status: str) -> None:
        self.set_id_pagamento(id_pagamento)
        self.set_id_reserva(id_reserva)
        self.set_data_pagamento(data_pagamento)
        self.set_valor_total(valor_total)
        self.set_forma_pagamento(forma_pagamento)
        self.set_status(status)

    # Setters:
    @staticmethod
    def set_id_pagamento(self, id_pagamento: int) -> None: self._id_pagamento = id_pagamento

    @staticmethod
    def set_id_reserva(self, id_reserva: int) -> None: self._id_reserva = id_reserva

    @staticmethod
    def set_data_pagamento(self, data_pagamento: date) -> None: self._data_pagamento = data_pagamento

    @staticmethod
    def set_valor_total(self, valor_total: float) -> None: self._valor_total = valor_total

    @staticmethod
    def set_forma_pagamento(self, forma_pagamento: str) -> None: self._forma_pagamento = forma_pagamento

    @staticmethod
    def set_status(self, status: str) -> None: self._status = status

    # Getters:
    @staticmethod
    def get_id_pagamento(self) -> int: return self._id_pagamento

    @staticmethod
    def get_id_reserva(self) -> int: return self._id_reserva
    
    @staticmethod
    def get_data_pagamento(self) -> date: return self._data_pagamento
    
    @staticmethod
    def get_valor_total(self) -> float: return self._valor_total
    
    @staticmethod
    def get_forma_pagamento(self) -> str: return self._forma_pagamento
    
    @staticmethod
    def get_status(self) -> str: return self._status

    # Métodos:
    @staticmethod
    def to_dict(self) -> dict:
        return {
            "id_pagamento": self.get_id_pagamento(),
            "id_reserva": self.get_id_reserva(),
            "data_pagamento": self.get_data_pagamento(),
            "valor_total": self.get_valor_total(),
            "forma_pagamento": self.get_forma_pagamento(),
            "status": self.get_status()
        }
    
    @staticmethod
    def from_row() -> None:
        pass

    def processar_pagamento(self) -> bool:
        # Lógica para processar o pagamento
        if self.get_status() == "Pendente":
            self.set_status("Concluído")
            return True
        return False