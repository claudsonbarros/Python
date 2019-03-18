user='user2'
senha='welcome1'
ip='127.0.0.1'
bd='xe'
import cx_Oracle

con = cx_Oracle.connect(user,senha,ip,bd)

print(user)
print(con)