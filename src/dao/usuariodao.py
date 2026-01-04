from dao.dao import DAO
from models.usuario import Usuario

class UsuarioDAO(DAO):
    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        sql = """
            INSERT INTO usuario (nome, fone, email, senha, perfil_tipo, perfil_id)
            VALUES (?, ?, ?, ?, ?, ?)
        """
        cls.execute(sql, (obj.get_nome(), obj.get_fone(), obj.get_email(), obj.get_senha(), obj.get_tipo_perfil(), obj.get_id_perfil()))
        cls.fechar()

    @classmethod
    def listar(cls):
        cls.abrir()
        sql = "SELECT * FROM usuario"
        cursor = cls.execute(sql)
        rows = cursor.fetchall()
        objs = [
            Usuario(idusuario, nome, fone, email, senha, tipoperfil, idperfil)
            for (idusuario, nome, fone, email, senha, tipoperfil, idperfil) in rows
        ]
        
        return objs

    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        sql = "SELECT * FROM usuario WHERE id = ?"
        cursor = cls.execute(sql, (id,))
        row = cursor.fetchone()
        obj = Usuario(*row) if row else None
        cls.fechar()
        return obj

    @classmethod
    def atualizar(cls, obj):
        cls.abrir()
        sql = """
            UPDATE usuario
            SET nome=?, fone=?, email=?, perfil_tipo=?, perfil_id=?
            WHERE id=?
        """
        cls.execute(sql, (
            obj.get_nome(),
            obj.get_fone(),
            obj.get_email(),
            obj.get_tipo_perfil(),
            obj.get_id_perfil(),
            obj.get_id_usuario()
        ))
    
    @classmethod
    def atualizar_senha(cls, obj):
        cls.abrir()
        sql = """
            UPDATE usuario
            SET senha=?
            WHERE id=?
        """
        cls.execute(sql, (
            obj.get_senha(),
            obj.get_id_usuario()
        ))

    @classmethod
    def excluir(cls, obj):
        cls.abrir()
        sql = "DELETE FROM usuario WHERE id=?"
        cls.execute(sql, (obj.get_id_usuario(),))
        cls.fechar()
