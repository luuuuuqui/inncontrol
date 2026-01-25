from dao.dao import DAO
from models.reserva import Reserva


class ReservaDAO(DAO):
    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        sql = """
            INSERT INTO reserva (id_hospede, id_quarto, data_checkin, data_checkout, status)
            VALUES (?, ?, ?, ?, ?)
        """
        cls.execute(
            sql,
            (
                obj.get_id_hospede(),
                obj.get_id_quarto(),
                obj.get_data_checkin(),
                obj.get_data_checkout(),
                obj.get_status(),
            ),
        )
        cls.fechar()

    @classmethod
    def listar(cls):
        cls.abrir()
        sql = "SELECT * FROM reserva"
        cursor = cls.execute(sql)
        rows = cursor.fetchall()
        objs = [
            Reserva(
                id_reserva, id_hospede, id_quarto, data_checkin, data_checkout, status
            )
            for (
                id_reserva,
                id_hospede,
                id_quarto,
                data_checkin,
                data_checkout,
                status,
            ) in rows
        ]

        return objs

    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        sql = "SELECT * FROM reserva WHERE id = ?"
        cursor = cls.execute(sql, (id,))
        row = cursor.fetchone()
        obj = Reserva(*row) if row else None
        cls.fechar()
        return obj

    @classmethod
    def listar_por_hospede(cls, id_hospede):
        cls.abrir()
        sql = "SELECT * FROM reserva WHERE id_hospede = ?"
        cursor = cls.execute(sql, (id_hospede,))
        rows = cursor.fetchall()

        objs = [
            Reserva(id, id_hosp, id_q, d_in, d_out, status)
            for (id, id_hosp, id_q, d_in, d_out, status) in rows
        ]
        cls.fechar()
        return objs

    @classmethod
    def atualizar(cls, obj):
        cls.abrir()
        sql = """
            UPDATE reserva
            SET id_hospede=?, id_quarto=?, data_checkin=?, data_checkout=?, status=?
            WHERE id=?
        """
        cls.execute(
            sql,
            (
                obj.get_id_hospede(),
                obj.get_id_quarto(),
                obj.get_data_checkin(),
                obj.get_data_checkot(),
                obj.get_status(),
                obj.get_id_reserva(),
            ),
        )

    @classmethod
    def excluir(cls, obj):
        cls.abrir()
        sql = "DELETE FROM reserva WHERE id=?"
        cls.execute(sql, (obj.get_id_reserva(),))
        cls.fechar()
