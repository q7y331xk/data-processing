from config import RDS_HOST, RDS_USER_NAME, RDS_USER_PW, RDS_DB, RDS_TABLE
import pymysql

def conn_db():
    conn = pymysql.connect(host=RDS_HOST, user=RDS_USER_NAME, password=RDS_USER_PW, charset='utf8', port=3306, db=RDS_DB)
    return conn

def read(table):
    conn = conn_db()
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {table}")
    rows_exist = cursor.fetchall()
    conn.commit()
    return rows_exist