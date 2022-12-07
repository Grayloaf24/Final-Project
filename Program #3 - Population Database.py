#Programmer: Gracie Lougheed, Natalie Thumberger, Guinevere Daniels
#Date: December 7, 2022
#Program Title: Population Database

import sqlite3

conn = sqlite3.connect('population.db')
cur = conn.cursor()

def main():
    cur.execute('''CREATE TABLE Population(city_id TEXT PRIMARY KEY NOT NULL, city_name TEXT, population INTEGER)''')
    cur.execute('''INSERT INTO Population(city_id, city_name, population) VALUES('01295224', 'Austin', 964177)''')
    cur.execute('SELECT city_id, city_name, population FROM Population')
    results = cur.fetchall()
    cur.execute('''INSERT INTO Population(city_id, city_name, population) VALUES('95825931', 'Columbus', 905860)''')
    cur.execute('SELECT city_id, city_name, population FROM Population')
    results = cur.fetchall()
    cur.execute('''INSERT INTO Population(city_id, city_name, population) VALUES('29682703', 'Boston', 654776)''')
    cur.execute('SELECT city_id, city_name, population FROM Population')
    results = cur.fetchall()
    order = "SELECT * FROM Population ORDER BY city_name"
    cur.execute(order)
    results = cur.fetchall()
    average = "SELECT AVG(population) AS average from Population"
    cur.execute(average)
    rows = cur.fetchall()
    for i in rows:
        print(f'Average marks is: {float(i[0]):.2f}')
    cur.execute("SELECT MIN(population) FROM Population")
    lowest = cur.fetchall()
    for i in lowest:
        print(f'City with the lowest population: {float(i[0]):.2f}')
    print('City       City Name   Population')
    for row in results:
        print(f'{row[0]:10} {row[1]:10} {row[2]:10.2f}')

    conn.commit()
    conn.close()

if __name__ == '__main__':
    main()