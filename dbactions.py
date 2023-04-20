import sqlite3

def connect_db():
    connection_db = sqlite3.connect("results.db")
    return connection_db