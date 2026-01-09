from dao.dao import DAO
from models.adicional import Adicional


class AdicionalDAO(DAO):
    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        sql = """
            INSERT INTO adicional (descricao, valor)
            VALUES (?, ?)
        """
        cls.execute(sql, (obj.get_descricao(), obj.get_valor()))
        cls.fechar()

    @classmethod
    def listar(cls):
        cls.abrir()
        sql = "SELECT * FROM adicional"
        cursor = cls.execute(sql)
        rows = cursor.fetchall()
        objs = [
            Adicional(id_adicional, descricao, valor)
            for (id_adicional, descricao, valor) in rows
        ]

        return objs

    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        sql = "SELECT * FROM adicional WHERE id = ?"
        cursor = cls.execute(sql, (id,))
        row = cursor.fetchone()
        obj = Adicional(*row) if row else None
        cls.fechar()
        return obj

    @classmethod
    def atualizar(cls, obj):
        cls.abrir()
        sql = """
            UPDATE adicional
            SET descricao=?, valor=?
            WHERE id=?
        """
        cls.execute(
            sql, (obj.get_descricao(), obj.get_valor(), obj.get_id_adicional())
        )

    @classmethod
    def excluir(cls, obj):
        cls.abrir()
        sql = "DELETE FROM adicional WHERE id=?"
        cls.execute(sql, (obj.get_id_adicional(),))
        cls.fechar()
