import cx_Oracle
#'user2/welcome1@127.0.0.1/xe'
user = 'user2'
senha = 'welcome1'
ip = '127.0.0.1'
port = 1521
SID = 'xe'


def openCon():
    global con
    con = cx_Oracle.connect(f'{user}/{senha}@{ip}/{SID}')

def closeCon():
    con.close()
#consul = "insert into regions (region_id,region_name) VALUES (1,'Norte');"
