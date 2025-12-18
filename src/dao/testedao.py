from dao.dao import DAO
from models.teste import Teste

class TesteDAO(DAO):
    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        sql = """
            INSERT INTO teste (name)
            VALUES (?)
        """
        cls.execute(sql, (obj.get_name(),))
        cls.fechar()

    @classmethod
    def listar(cls):
        cls.abrir()
        sql = "SELECT * FROM teste"
        cursor = cls.execute(sql)
        rows = cursor.fetchall()
        objs = [Teste(id, name) for (id, name) in rows]
        cls.fechar()
        return objs

    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        sql = "SELECT * FROM teste WHERE id = ?"
        cursor = cls.execute(sql, (id,))
        row = cursor.fetchone()
        obj = Teste(*row) if row else None
        cls.fechar()
        return obj

    @classmethod
    def atualizar(cls, obj):
        cls.abrir()
        sql = """
            UPDATE teste SET name=?
            WHERE id=?
        """
        cls.execute(sql, (obj.get_name(), obj.get_id()))
        cls.fechar()

    @classmethod
    def excluir(cls, obj):
        cls.abrir()
        sql = "DELETE FROM teste WHERE id=?"
        cls.execute(sql, (obj.get_id(),))
        cls.fechar()
