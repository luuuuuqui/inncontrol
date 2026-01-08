from dao.dao import DAO
from models.quarto import Quarto


class QuartoDAO(DAO):
    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        sql = """
            INSERT INTO quarto (id_tipo, bloco, numero)
            VALUES (?, ?, ?)
        """
        cls.execute(
            sql,
            (obj.get_id_quarto_tipo(), obj.get_bloco(), obj.get_numero()),
        )
        cls.fechar()

    @classmethod
    def listar(cls):
        cls.abrir()
        sql = "SELECT * FROM quarto"
        cursor = cls.execute(sql)
        rows = cursor.fetchall()
        objs = [
            Quarto(idquarto, id_tipo, bloco, numero)
            for (idquarto, id_tipo, bloco, numero) in rows
        ]
        return objs

    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        sql = "SELECT * FROM quarto WHERE id = ?"
        cursor = cls.execute(sql, (id,))
        row = cursor.fetchone()
        obj = Quarto(*row) if row else None
        cls.fechar()
        return obj

    @classmethod
    def atualizar(cls, obj):
        cls.abrir()
        sql = """
            UPDATE quarto
            SET id_tipo=?, bloco=?, numero=?
            WHERE id=?
        """
        cls.execute(
            sql,
            (obj.get_id_quarto_tipo(), obj.get_bloco(), obj.get_numero(), obj.get_id_quarto()),
        )

    @classmethod
    def excluir(cls, obj):
        cls.abrir()
        sql = "DELETE FROM quarto WHERE id=?"
        cls.execute(sql, (obj.get_id_quarto(),))
        cls.fechar()
