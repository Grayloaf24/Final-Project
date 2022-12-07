#Programmers: Gracie Lougheed, Natalie Thumberger, Guinevere Daniels
#Date: December 7, 2022
#Program Title: Textbook Access

import sqlite3 as lite
import sys

conn = lite.connect('textbooks.db')

with conn:
    cur = conn.cursor()
    cur.execute('INSERT INTO author VALUES("5", "Corrie", "Ten Boom", "19 Bartel St", "Harlem", "Holland", "2237")')
    cur.execute('SELECT * FROM author')
    rows = cur.fetchall()
    for row in rows:
        print(row)

    print()

    cur.execute('UPDATE author SET author_city = "Bedfordshire" WHERE author_id = "3"')
    cur.execute('SELECT * FROM author')
    rows = cur.fetchall()
    for row in rows:
        print(row)

    print()

    cur.execute('DELETE FROM author WHERE author_id = "2"')
    cur.execute('SELECT * FROM author')
    rows = cur.fetchall()
    for row in rows:
        print(row)

    conn.close()