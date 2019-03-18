import DBconect

def comGet(consulta):
    DBconect.openCon()
    cursor = DBconect.con.cursor()  # cria cursor
    cursor.execute(consulta)  # consulta sql
    result = cursor.fetchone()  # busca resultados da consulta
    return result  # imprime o resultado

    # print(con.version)
    cursor.close()


def comSet(consulta):
    # con = cx_Oracle.connect('user2/welcome1@127.0.0.1/xe')
    DBconect.openCon()
    cursor = DBconect.con.cursor()  # cria cursor
    cursor.execute(consulta)
    DBconect.con.commit()
    cursor.close()
