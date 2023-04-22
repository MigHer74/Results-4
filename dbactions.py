import sqlite3

def connect_db():
    connection_db = sqlite3.connect("results.db")
    return connection_db

def verify_tbl():
    cnx = connect_db()
    cur = cnx.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS "games" (
	gtype	VARCHAR(1),
	gweek	VARCHAR(2),
	ggame	INT,
	n1	INT,
	n2	INT,
	n3	INT,
	n4	INT,
	n5	INT,
	n6	INT)""")
    cnx.commit()
    cnx.close()

def check_data():
    cnx = connect_db()
    cur = cnx.cursor()
    cur.execute("SELECT * FROM games")
    curData = cur.fetchall()

    return curData