#Programmers: Natalie Thumberger, Guinevere Daniels, Gracie Lougheed
#Date: November 30, 2022
#Program Title: Student Info Database

import sqlite3

def main():
    conn = sqlite3.connect('StudentInfo.db')
    cur = conn.cursor()
    cur.execute('''CREATE TABLE Student(student_id TEXT PRIMARY KEY NOT NULL, first_name TEXT, last_name TEXT, 
                major TEXT, phone_number TEXT, email TEXT, gpa REAL)''')
    cur.execute('''INSERT INTO Student(student_id, first_name, last_name, major, phone_number, email, gpa)
                VALUES('01793452', 'Emily', 'Rivera', 'Business', '912-424-8924', 
                'eerivera@students.unwsp.edu', 3.72)''')
    cur.execute('SELECT student_id, first_name, last_name, major, phone_number, email, gpa FROM Student')
    results = cur.fetchall()
    cur.execute('''INSERT INTO Student(student_id, first_name, last_name, major, phone_number, email, gpa)
                    VALUES('03957295', 'Olive', 'Smith', 'Biochemical Engineering', '284-105-7632', 
                    'oasmith@students.unwsp.edu', 4.00)''')
    cur.execute('SELECT student_id, first_name, last_name, major, phone_number, email, gpa FROM Student')
    results = cur.fetchall()
    cur.execute('''INSERT INTO Student(student_id, first_name, last_name, major, phone_number, email, gpa)
                    VALUES('02948572', 'Mark', 'Wilson', 'Mechanical Engineering', '285-385-3852', 
                    'mhwilson@students.unwsp.edu', 3.14)''')
    cur.execute('SELECT student_id, first_name, last_name, major, phone_number, email, gpa FROM Student')
    results = cur.fetchall()
    print('Student    First Name Last Name  Major                     Phone Number    Email                             GPA')
    for row in results:
        print(f'{row[0]:10} {row[1]:10} {row[2]:10} {row[3]:25} {row[4]:15} {row[5]:15} {row[6]:10.2f}')

    conn.commit()
    conn.close()

if __name__ == '__main__':
    main()