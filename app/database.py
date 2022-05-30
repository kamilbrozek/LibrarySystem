import sqlite3


tmp_querry = "select * from users"


def execute(querry):
    try:
        connection = sqlite3.connect('local.db')
        cursor = connection.cursor()
        cursor.execute(querry)
        connection.commit()
    except sqlite3.Error as error:
        print("SQLite problem\; ", error)
    finally:
        connection.close()



def initDB():
    queries = [
        "CREATE TABLE IF NOT EXISTS Users (id INTEGER PRIMARY KEY AUTOINCREMENT, username VARCHAR, firstname VARCHAR, lastname VARCHAR, email VARCHAR, phone VARCHAR);",
        "CREATE TABLE IF NOT EXISTS Books (id INTEGER PRIMARY KEY AUTOINCREMENT, isbn VARCHAR, author VARCHAR, title VARCHAR, releasedate DATE, pages INT);",
        "CREATE TABLE IF NOT EXISTS Borrow (id INTEGER NOT NULL PRIMARY KEY,	userid INTEGER NOT NULL, bookid INTEGER NOT NULL, FOREIGN KEY (userid) REFERENCES Users(id), FOREIGN KEY (bookid) REFERENCES Books(id));"
    ]
    for querry in queries:
        execute(querry)

def deleteDB():
    queries = [
        "DROP TABLE IF EXISTS Borrow",
        "DROP TABLE IF EXISTS Users;",
        "DROP TABLE IF EXISTS Books;"
    ]
    for querry in queries:
        execute(querry)