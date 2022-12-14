#Programmers: Gracie Lougheed, Guinevere Daniels, Natalie Thumberger
#Date: December 14, 2022
#Program Title: Student Info Update

import sqlite3 as lite
import sys

conn = lite.connect('StudentInfo.db')

with conn:
    cur = conn.cursor()
    id = input('Enter student id you want to update: ')
    cur.execute("SELECT * FROM Student where student_id = '{}'".format(id))

    row = cur.fetchone()

    if(row==None):
        print("Not Found")
    else:
        print("Student: ", row[0])
        print("1]First Name: ", row[1])
        print('2]Last Name: ', row[2])
        print('3]Major: ', row[3])
        print('4]Phone Number: ', row[4])
        print('5]Email: ', row[5])
        print('6]GPA: ', row[6])
        print('7]Exit')
        change = input("Which field do you want to change? ")

        new_info = ""
        if(change=='1'):
            first_name = input('Enter New First Name: ')
            new_info = "first_name = '{}'".format(first_name)
        elif(change=='2'):
            last_name = input('Enter New Last Name: ')
            new_info = "last_name = '{}'".format(last_name)
        elif (change == '3'):
            major = input('Enter New Major: ')
            new_info = "Major = '{}'".format(major)
        elif (change == '4'):
            phone_number = input('Enter New Phone Number: ')
            new_info = "phone_number = '{}'".format(phone_number)
        elif (change == '5'):
            email = input('Enter New Email: ')
            new_info = "Email = '{}'".format(email)
        elif (change == '6'):
            gpa = input('Enter New GPA: ')
            new_info = "GPA = '{}'".format(gpa)
        elif(change == '7'):
            exit()
        else:
            print("Invalid Option")
        if(not new_info == ''):
            cur.execute("Update student set {} where student_id = {}".format(new_info, id))
            conn.commit()
            print('Record Updated')
        conn.close()