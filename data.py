import pymysql
from tabulate import tabulate

dbServerName = "localhost"
dbUser = "root"
dbPassword = "root123"
dbName = "shipu"
connection = pymysql.connect(host=dbServerName, user=dbUser, password=dbPassword, db=dbName)
cursor = connection.cursor()

def insert_(msg1, msg2):
    sql = ("""INSERT INTO shipu.error (pattern, responses) VALUES (%s, %s)""")
    ne = (msg1, msg2)
    cursor.execute(sql, ne)
    connection.commit()


def show_data():
    qu = "SELECT * FROM shipu.bot "
    cursor.execute(qu)
    rows = cursor.fetchall()
    print(tabulate(rows, headers=['pattern', 'responses'], tablefmt='psql'))

def delete__(msg):
    qu = """DELETE FROM `shipu`.`bot`WHERE (pattern=%s);"""
    #qe = "delete from bot where pattern={}".format(msg)
    cursor.execute(qu, msg)
    connection.commit()


#a = "ist eine Cloud sicher?"
#b = "Hallo, das lässt sich so nicht beantworten, darf ich noch ein paar Fragen stellen?"
#insert_(a, b)
#delete__("ist eine Cloud sicher?")
#show_data()
