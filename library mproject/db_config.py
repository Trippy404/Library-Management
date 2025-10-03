import pymysql as sql

def get_connection():
    return sql.connect(
        user="root",
        password="Ast@1230s",
        host="127.0.0.1",
        port=3306,
        database="library"
    )