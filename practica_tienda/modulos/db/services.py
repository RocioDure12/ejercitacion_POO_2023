import pymysql
from typing import List

class DBServices:
    def connect_db(self)-> pymysql.Connection:
        return pymysql.connect(
            host='localhost',
            port=3306,
            user='root',
            password='',
            database='tienda',
            cursorclass=pymysql.cursors.DictCursor

        )
        

    def execute_db(self, sql:str)->int:
        connection = self.connect_db()
        with connection.cursor() as cursor:
                cursor.execute(sql)
        connection.commit()
        return connection.affected_rows()
        
    
    def read_db(self, sql:str)->List[dict]:
       connection = self.connect_db()
       with connection.cursor() as cursor:
            cursor.execute(sql)
            return cursor.fetchall()