import os
import pymysql
from dotenv import load_dotenv

load_dotenv()


class MySQLConnector:
    _instance = None
    _connection = None

    def __init__(self):
        self.host = os.getenv("DB_HOST")
        self.user = os.getenv("DB_USER")
        self.password = os.getenv("DB_PASSWORD")
        self.database = os.getenv("DB_NAME")

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def get_connection(self):
        if not self._connection:
            self._connection = pymysql.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database,
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor
            )
        return self._connection

    def execute_select_query(self, query, params):
        try:
            connection = self.get_connection()
            cursor = connection.cursor()
            cursor.execute(query, params)
            result = cursor.fetchall()
            return result
        except pymysql.Error as err:
            print(f"Error: {err}")
        finally:
            cursor.close()

    def execute_query(self, query):
        try:
            connection = self.get_connection()
            cursor = connection.cursor()
            cursor.execute(query)
            result = cursor.fetchall()
            return result
        except pymysql.Error as err:
            print(f"Error: {err}")
        finally:
            cursor.close()
