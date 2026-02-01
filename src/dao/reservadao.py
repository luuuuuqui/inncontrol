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
        from datetime import datetime
        
        cls.abrir()
        sql = "SELECT * FROM reserva"
        cursor = cls.execute(sql)
        rows = cursor.fetchall()
        objs = []
        for (
            id_reserva,
            id_hospede,
            id_quarto,
            data_checkin,
            data_checkout,
            status,
        ) in rows:
            # Garantir que as datas sejam strings
            if isinstance(data_checkin, datetime):
                data_checkin = data_checkin.strftime("%Y-%m-%d")
            elif data_checkin is not None:
                data_checkin = str(data_checkin)
            
            if isinstance(data_checkout, datetime):
                data_checkout = data_checkout.strftime("%Y-%m-%d")
            elif data_checkout is not None:
                data_checkout = str(data_checkout)
            
            objs.append(
                Reserva(
                    id_reserva, id_hospede, id_quarto, data_checkin, data_checkout, status
                )
            )

        return objs

    @classmethod
    def listar_id(cls, id):
        from datetime import datetime
        
        cls.abrir()
        sql = "SELECT * FROM reserva WHERE id = ?"
        cursor = cls.execute(sql, (id,))
        row = cursor.fetchone()
        if row:
            id_reserva, id_hospede, id_quarto, data_checkin, data_checkout, status = row
            # Garantir que as datas sejam strings
            if isinstance(data_checkin, datetime):
                data_checkin = data_checkin.strftime("%Y-%m-%d")
            elif data_checkin is not None:
                data_checkin = str(data_checkin)
            
            if isinstance(data_checkout, datetime):
                data_checkout = data_checkout.strftime("%Y-%m-%d")
            elif data_checkout is not None:
                data_checkout = str(data_checkout)
            
            obj = Reserva(id_reserva, id_hospede, id_quarto, data_checkin, data_checkout, status)
        else:
            obj = None
        cls.fechar()
        return obj

    @classmethod
    def listar_por_hospede(cls, id_hospede):
        from datetime import datetime
        
        cls.abrir()
        sql = "SELECT * FROM reserva WHERE id_hospede = ?"
        cursor = cls.execute(sql, (id_hospede,))
        rows = cursor.fetchall()

        objs = []
        for (id, id_hosp, id_q, d_in, d_out, status) in rows:
            # Garantir que as datas sejam strings
            if isinstance(d_in, datetime):
                d_in = d_in.strftime("%Y-%m-%d")
            elif d_in is not None:
                d_in = str(d_in)
            
            if isinstance(d_out, datetime):
                d_out = d_out.strftime("%Y-%m-%d")
            elif d_out is not None:
                d_out = str(d_out)
            
            objs.append(Reserva(id, id_hosp, id_q, d_in, d_out, status))
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
                obj.get_data_checkout(),
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
