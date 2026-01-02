from dao.dao import DAO
from models.hospede import Hospede

class HospedeDAO(DAO):
    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        sql = """
            INSERT INTO hospede (id_usuario, endereco)
            VALUES (?, ?)
        """
        cls.execute(sql, (obj.get_id_usuario(), obj.get_endereco()))
        cls.fechar()

    @classmethod
    def listar(cls):
        cls.abrir()
        sql = "SELECT * FROM hospede"
        cursor = cls.execute(sql)
        rows = cursor.fetchall()
        objs = [
            Hospede(id_hospede, id_usuario, endereco)
            for (id_hospede, id_usuario, endereco) in rows
        ]
        
        return objs

    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        sql = "SELECT * FROM hospede WHERE id = ?"
        cursor = cls.execute(sql, (id,))
        row = cursor.fetchone()
        obj = Hospede(*row) if row else None
        cls.fechar()
        return obj

    @classmethod
    def atualizar(cls, obj):
        cls.abrir()
        sql = """
            UPDATE hospede
            SET id_usuario=?, endereco=?
            WHERE id=?
        """
        cls.execute(sql, (
            obj.get_id_usuario(),
            obj.get_endereco(),
            obj.get_id_hospede()
        ))

    @classmethod
    def excluir(cls, obj):
        cls.abrir()      
        sql = "DELETE FROM hospede WHERE id=?"
        cls.execute(sql, (obj.get_id_hospede(),))
        cls.fechar()
