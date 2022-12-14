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
                VALUES('1', 'Emily', 'Rivera', 'Business', '912-424-8924', 
                'eerivera@students.unwsp.edu', 3.72)''')
    cur.execute('SELECT student_id, first_name, last_name, major, phone_number, email, gpa FROM Student')
    results = cur.fetchall()
    cur.execute('''INSERT INTO Student(student_id, first_name, last_name, major, phone_number, email, gpa)
                    VALUES('2', 'Olive', 'Smith', 'Biochemical Engineering', '284-105-7632', 
                    'oasmith@students.unwsp.edu', 4.00)''')
    cur.execute('SELECT student_id, first_name, last_name, major, phone_number, email, gpa FROM Student')
    results = cur.fetchall()
    cur.execute('''INSERT INTO Student(student_id, first_name, last_name, major, phone_number, email, gpa)
                    VALUES('3', 'Mark', 'Wilson', 'Mechanical Engineering', '285-385-3852', 
                    'mhwilson@students.unwsp.edu', 3.14)''')
    cur.execute('SELECT student_id, first_name, last_name, major, phone_number, email, gpa FROM Student')
    results = cur.fetchall()
    cur.execute('''INSERT INTO Student(student_id, first_name, last_name, major, phone_number, email, gpa)
                        VALUES('4', 'Felicia', 'Paulson', 'History', '950-295-2719', 
                        'fwpaulson@students.unwsp.edu', 2.86)''')
    cur.execute('SELECT student_id, first_name, last_name, major, phone_number, email, gpa FROM Student')
    results = cur.fetchall()
    cur.execute('''INSERT INTO Student(student_id, first_name, last_name, major, phone_number, email, gpa)
                        VALUES('5', 'Logan', 'Sathare', 'Economics', '126-507-8243', 
                        'lisathare@students.unwsp.edu', 2.34)''')
    cur.execute('SELECT student_id, first_name, last_name, major, phone_number, email, gpa FROM Student')
    results = cur.fetchall()
    cur.execute('''INSERT INTO Student(student_id, first_name, last_name, major, phone_number, email, gpa)
                        VALUES('6', 'Jade', 'Rentons', 'Accounting', '195-275-3862', 
                        'jtrentons@students.unwsp.edu', 3.25)''')
    cur.execute('SELECT student_id, first_name, last_name, major, phone_number, email, gpa FROM Student')
    results = cur.fetchall()
    cur.execute('''INSERT INTO Student(student_id, first_name, last_name, major, phone_number, email, gpa)
                        VALUES('7', 'Kristin', 'Hilton', 'Anthropology', '718-592-3061', 
                        'kfhilton@students.unwsp.edu', 3.00)''')
    cur.execute('SELECT student_id, first_name, last_name, major, phone_number, email, gpa FROM Student')
    results = cur.fetchall()
    cur.execute('''INSERT INTO Student(student_id, first_name, last_name, major, phone_number, email, gpa)
                        VALUES('8', 'Henry', 'Trenton', 'Marketing', '528-769-0183', 
                        'hgtrenton@students.unwsp.edu', 2.51)''')
    cur.execute('SELECT student_id, first_name, last_name, major, phone_number, email, gpa FROM Student')
    results = cur.fetchall()
    cur.execute('''INSERT INTO Student(student_id, first_name, last_name, major, phone_number, email, gpa)
                        VALUES('9', 'Alex', 'Preston', 'Computer Engineering', '916-296-2986', 
                        'alpreston@students.unwsp.edu', 3.97)''')
    cur.execute('SELECT student_id, first_name, last_name, major, phone_number, email, gpa FROM Student')
    results = cur.fetchall()
    cur.execute('''INSERT INTO Student(student_id, first_name, last_name, major, phone_number, email, gpa)
                        VALUES('10', 'Luna', 'Preston', 'Civil Engineering', '284-105-7632', 
                        'lapreston@students.unwsp.edu', 4.00)''')
    cur.execute('SELECT student_id, first_name, last_name, major, phone_number, email, gpa FROM Student')
    results = cur.fetchall()
    print('Student    First Name Last Name  Major                     Phone Number    Email                             GPA')
    for row in results:
        print(f'{row[0]:10} {row[1]:10} {row[2]:10} {row[3]:25} {row[4]:15} {row[5]:15} {row[6]:10.2f}')

    conn.commit()
    conn.close()

if __name__ == '__main__':
    main()

    #update = input("Would you like to update the student records? ")
    #if update == 'Yes':
        #field = input('Enter what field you want updated: ')
        #student = input('Enter what student you want to change the info of: ')
        #info = input('Enter what info you want changed: ')
        #cur.execute('UPDATE Student SET field = info WHERE student_id = student')
        #cur.execute('SELECT * FROM Student')
        #rows = cur.fetchall()
        #for row in rows:
            #print(row)
    #else:
        #pass