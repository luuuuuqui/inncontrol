import sqlite3
import os


class Database:
    conn = None
    basedirectory = os.path.dirname(os.path.abspath(__file__))
    pathdb = os.path.join(basedirectory, "inncontrol.db")

    @classmethod
    def abrir(cls):
        cls.conn = sqlite3.connect(cls.pathdb, check_same_thread=False)
        cls.conn.execute("PRAGMA foreign_keys = ON")

    @classmethod
    def fechar(cls):
        if cls.conn:
            cls.conn.close()
        else:
            raise Exception("Conexão não estabelecida.")

    @classmethod
    def execute(cls, sql, params=None):
        if not cls.conn:
            raise Exception("Conexão não estabelecida.")
        cursor = cls.conn.cursor()
        cursor.execute(sql, params or [])
        cls.conn.commit()
        return cursor

    @classmethod
    def criar_tabelas(cls):
        cls.abrir()

        # criar a tabela usuário
        cls.execute(
            """
        CREATE TABLE IF NOT EXISTS usuario (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            fone TEXT,
            email TEXT NOT NULL UNIQUE,
            senha TEXT NOT NULL,
            perfil_tipo TEXT NOT NULL
        );
        """
        )

        # criar a tabela hóspede
        cls.execute(
            """
        CREATE TABLE IF NOT EXISTS hospede (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            id_usuario INTEGER NOT NULL,
            endereco TEXT NOT NULL,
            FOREIGN KEY (id_usuario) REFERENCES usuario (id)
        );
        """
        )

        # criar a tabela quarto
        cls.execute(
            """
        CREATE TABLE IF NOT EXISTS quarto (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            id_tipo INTEGER NOT NULL,
            bloco TEXT NOT NULL,
            numero INTEGER NOT NULL,
            FOREIGN KEY (id_tipo) REFERENCES tipoquarto (id)
        );
        """
        )

        # criar a tabela tipo de quarto
        cls.execute(
            """
        CREATE TABLE IF NOT EXISTS tipoquarto (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL UNIQUE,
            descricao TEXT NOT NULL,
            capacidade INTEGER NOT NULL,
            valor_diaria TEXT NOT NULL
        );
        """
        )

        # criar a tabela reserva
        cls.execute(
            """
        CREATE TABLE IF NOT EXISTS reserva (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            id_hospede INTEGER NOT NULL,
            id_quarto INTEGER NOT NULL,
            data_checkin TEXT NOT NULL,
            data_checkout TEXT NOT NULL,
            status TEXT NOT NULL,
            FOREIGN KEY (id_hospede) REFERENCES hospede (id),
            FOREIGN KEY (id_quarto) REFERENCES quarto (id)
        );
        """
        )

        # criar a tabela pagamento
        cls.execute(
            """
        CREATE TABLE IF NOT EXISTS pagamento (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            id_reserva INTEGER NOT NULL,
            data_pagamento TEXT NOT NULL,
            valor_total TEXT NOT NULL,
            forma_pagamento TEXT NOT NULL,
            status TEXT NOT NULL,
            FOREIGN KEY (id_reserva) REFERENCES reserva (id)
        );
        """
        )

        # criar a tabela consumo
        cls.execute(
            """
        CREATE TABLE IF NOT EXISTS consumo (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            id_reserva INTEGER NOT NULL,
            id_adicional INTEGER NOT NULL,
            quantidade INTEGER NOT NULL,
            data_consumo TEXT NOT NULL,
            FOREIGN KEY (id_adicional) REFERENCES adicional (id)
            FOREIGN KEY (id_reserva) REFERENCES reserva (id)
        );
        """
        )

        # criar a tabela adicional
        cls.execute(
            """
        CREATE TABLE IF NOT EXISTS adicional (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            descricao TEXT NOT NULL,
            valor TEXT NOT NULL
        );
        """
        )

        cls.fechar()
