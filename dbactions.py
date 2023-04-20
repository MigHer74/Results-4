import sqlite3

def connect_db():
    connection_db = sqlite3.connect("results.db")
    return connection_db

def create_tbl():
    cnx = connect_db()
    cur = cnx.cursor()
    scpFile = open("table.sql")
    scpVar = scpFile.read()
    cur.executescript(scpVar)
    cnx.commit()
    cnx.close()