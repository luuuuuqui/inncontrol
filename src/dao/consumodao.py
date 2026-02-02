from dao.dao import DAO
from models.consumo import Consumo


class ConsumoDAO(DAO):
    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        sql = """
            INSERT INTO consumo (id_reserva, id_adicional, quantidade, data_consumo)
            VALUES (?, ?, ?, ?)
        """
        cls.execute(
            sql,
            (
                obj.get_id_reserva(),
                obj.get_id_adicional(),
                obj.get_quantidade(),
                obj.get_data_consumo(),
            ),
        )
        cls.fechar()

    @classmethod
    def listar(cls):
        cls.abrir()
        sql = "SELECT * FROM consumo"
        cursor = cls.execute(sql)
        rows = cursor.fetchall()
        objs = [
            Consumo(id_consumo, id_reserva, id_adicional, quantidade, data_consumo)
            for (id_consumo, id_reserva, id_adicional, quantidade, data_consumo) in rows
        ]

        return objs

    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        sql = "SELECT * FROM consumo WHERE id = ?"
        cursor = cls.execute(sql, (id,))
        row = cursor.fetchone()
        obj = Consumo(*row) if row else None
        cls.fechar()
        return obj

    @classmethod
    def listar_por_reserva(cls, id_reserva):
        cls.abrir()
        sql = "SELECT * FROM consumo WHERE id_reserva = ?"
        cursor = cls.execute(sql, (id_reserva,))
        rows = cursor.fetchall()
        objs = [
            Consumo(id_consumo, id_reserva, id_adicional, quantidade, data_consumo)
            for (id_consumo, id_reserva, id_adicional, quantidade, data_consumo) in rows
        ]
        cls.fechar()
        return objs

    @classmethod
    def atualizar(cls, obj):
        cls.abrir()
        sql = """
            UPDATE consumo
            SET id_reserva=?, id_adicional=?, quantidade=?, data_consumo=?
            WHERE id=?
        """
        cls.execute(
            sql,
            (
                obj.get_id_reserva(),
                obj.get_id_adicional(),
                obj.get_quantidade(),
                obj.get_data_consumo(),
                obj.get_id_consumo(),
            ),
        )

    @classmethod
    def excluir(cls, obj):
        cls.abrir()
        sql = "DELETE FROM consumo WHERE id=?"
        cls.execute(sql, (obj.get_id_consumo(),))
        cls.fechar()
