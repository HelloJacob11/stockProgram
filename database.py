import sqlite3
def connect_DB(db_name):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    print(f"{db_name} connect!")
    return conn, cursor

def sql_exe(cursor,sql,conn,para=None):
    #print(sql,para)
    if para:
        cursor.execute(sql,para)
    else:
        print(sql)
        cursor.execute(sql)
    conn.commit()

def get_data(sql,cursor):
    cursor.execute(sql)
    rows = cursor.fetchall()
    return rows
