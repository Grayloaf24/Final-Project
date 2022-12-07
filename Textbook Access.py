#Programmers: Gracie Lougheed, Natalie Thumberger, Guinevere Daniels
#Date: December 7, 2022
#Program Title: Textbook Access

import sqlite3 as lite
import sys

conn = lite.connect('textbooks.db')

with conn:
    cur = conn.cursor()
    cur.execute("SELECT * FROM author")
    rows = cur.fetchall()
    for row in rows:
        print(row)

    conn.close()