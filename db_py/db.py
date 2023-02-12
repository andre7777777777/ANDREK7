import sqlite3


class Database:
    def __init__(self, path_to_db="data.sqlite"):
        self.path_to_db = path_to_db

    @property
    def connection(self):
        return sqlite3.connect(self.path_to_db)

    def execute(self, sql: str, parameters: tuple = None, fetchone=False, fetchall=False, commit=False):
        if not parameters:
            parameters = ()
        connection = self.connection
        cursor = connection.cursor()
        data = None
        cursor.execute(sql, parameters)

        if commit:
            connection.commit()
        if fetchall:
            data = cursor.fetchall()
        if fetchone:
            data = cursor.fetchone()
        connection.close()
        return data

    def create_table_users(self):
        sql = """
        CREATE TABLE IF NOT EXISTS Users (
            user_id integer PRIMARY KEY,
            username varchar(255),
            name varchar(255),
            date varchar(255)
            );
        CREATE TABLE IF NOT EXISTS Block(
            user_id integer PRIMARY KEY
        )
"""
        self.execute(sql, commit=True)

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = ?" for item in parameters
        ])
        return sql, tuple(parameters.values())

    def add_user(self, user_id: int, username: str, name: str, date: str):
        sql = """
        INSERT INTO Users(user_id, username, name, date) VALUES(?, ?, ?, ?)
        """
        self.execute(sql, parameters=(user_id, username, name, date), commit=True)

    def select_all_users(self):
        sql = """
        SELECT * FROM Users
        """
        return self.execute(sql, fetchall=True)

    def add_user_to_block(self, user_id: int):
        sql = """
        INSERT INTO Block(user_id) VALUES(?)
        """
        return self.execute(sql, parameters=(user_id), commit=True)

    def select_all_users_in_block(self):
        sql = """
        SELECT * FROM Block
        """
        return self.execute(sql, fetchall=True)

    def delete_user_in_block(self, user_id: int):
        sql = """
        DELETE FROM Block
        WHERE user_id=?
        """
        return self.execute(sql, parameters=(user_id), commit=True)
