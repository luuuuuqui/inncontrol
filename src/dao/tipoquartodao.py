from dao.dao import DAO
from models.tipoquarto import TipoQuarto


class TipoQuartoDAO(DAO):
    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        sql = """
            INSERT INTO tipoquarto (nome, descricao, capacidade, valor_diaria)
            VALUES (?, ?, ?, ?)
        """
        cls.execute(
            sql,
            (
                obj.get_nome(),
                obj.get_descricao(),
                obj.get_capacidade(),
                obj.get_valor_diaria(),
            ),
        )
        cls.fechar()

    @classmethod
    def listar(cls):
        cls.abrir()
        sql = "SELECT * FROM tipoquarto"
        cursor = cls.execute(sql)
        rows = cursor.fetchall()
        objs = [
            TipoQuarto(idtipoquarto, nome, descricao, capacidade, valor_diaria)
            for (idtipoquarto, nome, descricao, capacidade, valor_diaria) in rows
        ]

        return objs

    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        sql = "SELECT * FROM tipoquarto WHERE id = ?"
        cursor = cls.execute(sql, (id,))
        row = cursor.fetchone()
        obj = TipoQuarto(*row) if row else None
        cls.fechar()
        return obj

    @classmethod
    def atualizar(cls, obj):
        cls.abrir()
        sql = """
            UPDATE tipoquarto
            SET nome=?, descricao=?, capacidade=?, valor_diaria=?
            WHERE id=?
        """
        cls.execute(
            sql,
            (
                obj.get_nome(),
                obj.get_descricao(),
                obj.get_capacidade(),
                obj.get_valor_diaria(),
                obj.get_id_tipoquarto(),
            ),
        )

    @classmethod
    def excluir(cls, obj):
        cls.abrir()
        sql = "DELETE FROM tipoquarto WHERE id=?"
        cls.execute(sql, (obj.get_id_tipoquarto(),))
        cls.fechar()
