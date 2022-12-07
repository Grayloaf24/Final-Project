#Programmer: Gracie Lougheed
#Date: November 30, 2022
#Program Title: Textbooks Database

import sqlite3

def main():
    conn = sqlite3.connect('textbooks.db')
    cur = conn.cursor()

    cur.execute('''CREATE TABLE Book(isbn TEXT PRIMARY KEY NOT NULL, publisher_id TEXT, author_id TEXT, title TEXT,
                print_date TEXT, price REAL)''')
    cur.execute('''INSERT INTO Book(isbn, publisher_id, author_id, title, print_date, price) VALUES('1049753', 
    'Pearson', 'Gaddis', 'Python Sixth Edition', '2020', 103.45)''')
    cur.execute('SELECT isbn, publisher_id, author_id, title, print_date, price FROM Book')
    results = cur.fetchall()
    cur.execute('''INSERT INTO Book(isbn, publisher_id, author_id, title, print_date, price) VALUES('5063472', 
        'Peerstone', 'Gladin', 'C++ First Edition  ', '2014', 73.99)''')
    cur.execute('SELECT isbn, publisher_id, author_id, title, print_date, price FROM Book')
    results = cur.fetchall()
    cur.execute('''INSERT INTO Book(isbn, publisher_id, author_id, title, print_date, price) VALUES('2051498', 
        'Reshire', 'Lockust', 'Java Seventh Edition', '2022', 94.62)''')
    cur.execute('SELECT isbn, publisher_id, author_id, title, print_date, price FROM Book')
    results = cur.fetchall()
    print('ISBN       Publisher  Author     Title                Date    Price')
    for row in results:
        print(f'{row[0]:10} {row[1]:10} {row[2]:10} {row[3]:10} {row[4]:5} {row[5]:8.2f}')

    cur.execute('''CREATE TABLE Publisher(publisher_id TEXT PRIMARY KEY NOT NULL, pub_name TEXT, pub_city TEXT, 
                pub_state TEXT, print_zip TEXT)''')
    cur.execute('''INSERT INTO Publisher(publisher_id, pub_name, pub_city, pub_state, print_zip) VALUES('Pearson', 
                'Kirsten Valburg', 'Austin', 'Texas', '71523')''')
    cur.execute('SELECT publisher_id, pub_name, pub_city, pub_state, print_zip FROM Publisher')
    results = cur.fetchall()
    cur.execute('''INSERT INTO Publisher(publisher_id, pub_name, pub_city, pub_state, print_zip) VALUES('Peerstone', 
            'Jason Stonewell', 'New York City', 'New York', '91052')''')
    cur.execute('SELECT publisher_id, pub_name, pub_city, pub_state, print_zip FROM Publisher')
    results = cur.fetchall()
    cur.execute('''INSERT INTO Publisher(publisher_id, pub_name, pub_city, pub_state, print_zip) VALUES('Reshire', 
            'Jeremy Miles', 'Juno', 'Alaska', '42963')''')
    cur.execute('SELECT publisher_id, pub_name, pub_city, pub_state, print_zip FROM Publisher')
    results = cur.fetchall()
    print('Publisher  Name                  City        State      Zip')
    for row in results:
        print(f'{row[0]:10} {row[1]:10} {row[2]:15} {row[3]:10} {row[4]:8}')

    cur.execute('''CREATE TABLE Author(author_id TEXT PRIMARY KEY NOT NULL, first_name TEXT, last_name TEXT, 
                author_address TEXT, author_city TEXT, author_state TEXT, author_zip TEXT)''')
    cur.execute('''INSERT INTO Author(author_id, first_name, last_name, author_address, author_city, author_state, 
                author_zip) VALUES('Gaddis', 'Henry', 'Gaddis', '328 Hillshire Drive', 'Houston', 'Texas', '75212')''')
    cur.execute('SELECT author_id, first_name, last_name, author_address, author_city, author_state, author_zip FROM Author')
    results = cur.fetchall()
    cur.execute('''INSERT INTO Author(author_id, first_name, last_name, author_address, author_city, author_state, 
                author_zip) VALUES('Gladin', 'Jade', 'Gladin', '195 Robin Road', 'Seattle', 'Washington', '81345')''')
    cur.execute('SELECT author_id, first_name, last_name, author_address, author_city, author_state, author_zip FROM Author')
    results = cur.fetchall()
    cur.execute('''INSERT INTO Author(author_id, first_name, last_name, author_address, author_city, author_state, 
                author_zip) VALUES('Lockust', 'Trenton', 'Lockust', '2853 Lizard Lane', 'Miami', 'Florida', '13952')''')
    cur.execute('SELECT author_id, first_name, last_name, author_address, author_city, author_state, author_zip FROM Author')
    results = cur.fetchall()
    print('Author     First Name  Last Name   Address                City    State      Zip')
    for row in results:
        print(f'{row[0]:10} {row[1]:10} {row[2]:10} {row[3]:10} {row[4]:15} {row[5]:8} {row[6]:5}')

    conn.commit()
    conn.close()

if __name__ == '__main__':
    main()
