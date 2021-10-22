import json
import pymysql
from tabulate import tabulate

dbServerName = "localhost"
dbUser = "root"
dbPassword = "root123"
dbName = "shipu"
connection = pymysql.connect(host=dbServerName, user=dbUser, password=dbPassword, db=dbName)
curs = connection.cursor()

with open("new_german.json") as file:
    data = json.load(file)


def convrt_json():
    for intent in data["intents"]:
        a, b, c, d, e, f, g = "", "", "", "", "", "", ""
        for s in intent["tag"]:
            a = a + s + ","
        for s in intent["patterns"]:
            b = b + s + ","
        for s in intent["responses"]:
            c = c + s + ","
        for s in intent["context_set"]:
            d = d + s + ","
        for s in intent["store_to_db"]:
            e = e + s + ","
        for s in intent["doc_path"]:
            f = f + s + ","
        for s in intent["open_path"]:
            g = g + s + ","

        #print(a, b, c, d, e, f, g)
        insert_(a, b, c, d, e, f, g)



def insert_(m1, m2, m3, m4, m5, m6, m7):
    curs = connection.cursor()
    sql = ("""INSERT INTO shipu.json_file(tag, patterns, responses, context_set, store_to_db, doc_path, open_path) VALUES (%s, %s, %s, %s, %s ,%s, %s)""")
    ne = (m1, m2, m3, m4, m5, m6, m7)
    curs.execute(sql, ne)
    print("inserted")
    connection.commit()

def delete__(msg):
    qu = """DELETE FROM `shipu`.`template` WHERE (tag=%s);"""
    #qe = "delete from bot where pattern={}".format(msg)
    curs.execute(qu, msg)
    connection.commit()

def create_db():
    curs = connection.cursor()
    sql = ("""CREATE TABLE `shipu`.`helloko` (
  `tag` VARCHAR(1000) NOT NULL,
  `patterns` VARCHAR(500) NOT NULL,
  `responses` VARCHAR(1500) NOT NULL,
  `context_set` VARCHAR(500) NOT NULL,
  `store_to_db` VARCHAR(200) NOT NULL,
  `doc_path` VARCHAR(500) NOT NULL,
  `open_path` VARCHAR(500) NOT NULL);""")
    curs.execute(sql)
    print("created")
    connection.commit()


def show_data():
    qu = "SELECT * FROM shipu.json_file"
    curs.execute(qu)
    rows = curs.fetchall()
    print(tabulate(rows, headers=['tag', 'pattern', 'responses', 'context_set', 'store_to_db', 'doc_path', 'open_path'], tablefmt='psql'))

#create_db()
#convrt_json()
#delete__("ja")
show_data()



