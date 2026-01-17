from dao.dao import DAO
from models.pagamento import Pagamento


class PagamentoDAO(DAO):
    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        sql = """
            INSERT INTO pagamento (id_reserva, data_pagamento, valor_total, forma_pagamento, status)
            VALUES (?, ?, ?, ?, ?)
        """
        cls.execute(
            sql,
            (
                obj.get_id_reserva(),
                obj.get_data_pagamento(),
                obj.get_valor_total(),
                obj.get_forma_pagamento(),
                obj.get_status(),
            ),
        )
        cls.fechar()

    @classmethod
    def listar(cls):
        cls.abrir()
        sql = "SELECT * FROM pagamento"
        cursor = cls.execute(sql)
        rows = cursor.fetchall()
        objs = [
            Pagamento(
                id_pagamento,
                id_reserva,
                data_pagamento,
                valor_total,
                forma_pagamento,
                status,
            )
            for (
                id_pagamento,
                id_reserva,
                data_pagamento,
                valor_total,
                forma_pagamento,
                status,
            ) in rows
        ]
        cls.fechar()

        return objs

    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        sql = "SELECT * FROM pagamento WHERE id = ?"
        cursor = cls.execute(sql, (id,))
        row = cursor.fetchone()
        obj = Pagamento(*row) if row else None
        cls.fechar()
        return obj
    
    @classmethod
    def listar_reserva(cls, id_reserva):
        cls.abrir()
        sql = "SELECT * FROM pagamento WHERE id_reserva = ?"
        cursor = cls.execute(sql, (id_reserva,))
        row = cursor.fetchone()
        obj = Pagamento(*row) if row else None
        cls.fechar()
        return obj

    @classmethod
    def atualizar(cls, obj):
        cls.abrir()
        sql = """
            UPDATE pagamento
            SET id_reserva=?, data_pagamento=?, forma_pagamento=?, status=?
            WHERE id=?
        """
        cls.execute(
            sql,
            (
                obj.get_id_reserva(),
                obj.get_data_pagamento(),
                obj.get_forma_pagamento(),
                obj.get_status(),
                obj.get_id_pagamento(),
            ),
        )
        cls.fechar()

    @classmethod
    def atualizar_valor(cls, obj):
        cls.abrir()
        sql = """
            UPDATE pagamento
            SET valor_total=?
            WHERE id=?
        """
        cls.execute(
            sql,
            (
                obj.get_valor_total(),
                obj.get_id_pagamento(),
            ),
        )
        cls.fechar()

    @classmethod
    def excluir(cls, obj):
        cls.abrir()
        sql = "DELETE FROM pagamento WHERE id=?"
        cls.execute(sql, (obj.get_id_pagamento(),))
        cls.fechar()
