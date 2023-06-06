import sqlite3


#create database task_manager
con = sqlite3.connect('task_manager.db')

#create cursor for task manager database
c = con.cursor()

#create table calendar which holds all information by date
c.execute('''CREATE TABLE IF NOT EXISTS calendar(
               name TEXT, 
               date TEXT,
               time TEXT,
               time_end TEXT,
               description TEXT,
               class TEXT,
               semester TEXT)''')


#create table assignments which holds all information about each assignment
c.execute('''CREATE TABLE IF NOT EXISTS assignments(
                name TEXT,
                class TEXT,
                date TEXT,
                time TEXT,
                priority INTEGER,
                description TEXT,
                status INTEGER)''')

#create table tests which holds all information about each test
c.execute('''CREATE TABLE IF NOT EXISTS tests(
                name TEXT,
                class TEXT,
                date TEXT,
                time TEXT,
                time_end TEXT,
                description TEXT,
                location TEXT)''')

#create table quizzes which holds all information about each quiz
c.execute('''CREATE TABLE IF NOT EXISTS quizzes(
                name TEXT,
                class TEXT,
                date TEXT,
                time TEXT,
                time_end TEXT,
                description TEXT,
                status INTEGER,
                location TEXT)''')

#create table appointments which holds all information about each appointment
c.execute('''CREATE TABLE IF NOT EXISTS appointments(
                name TEXT,
                location TEXT,
                date TEXT,
                time TEXT,
                time_end TEXT,
                description TEXT)''')

#create table tasks which holds all information about each task
c.execute('''CREATE TABLE IF NOT EXISTS tasks(
                name TEXT,
                priority INTEGER,
                date TEXT,
                time TEXT,
                status INTEGER,
                description TEXT)''')

#create table Classes which holds all information about each class
c.execute('''CREATE TABLE IF NOT EXISTS classes(
                name TEXT,
                time TEXT,
                time_end TEXT,
                dates TEXT,
                location TEXT,
                type TEXT,
                professor TEXT,
                semester TEXT,
                description TEXT)''')

#add a table for the days of the week of each class
c.execute('''CREATE TABLE IF NOT EXISTS class_days(
                class_name TEXT,
                date TEXT,
                date_end TEXT,
                sunday INTEGER,
                monday INTEGER,
                tuesday INTEGER,
                thursday INTEGER,
                friday INTEGER,
                saturday INTEGER,
                semester TEXT) ''')



#create table semesters which holds general information about each semester
c.execute('''CREATE TABLE IF NOT EXISTS semesters(
                name TEXT,
                date TEXT,
                date_end TEXT,
                classes TEXT)''')

#create table Events which holds all information about each event
c.execute('''CREATE TABLE IF NOT EXISTS events(
                name TEXT,
                location TEXT,
                date TEXT,
                date_end TEXT,
                time TEXT,
                time_end TEXT,
                description TEXT)''')

con.commit()
con.close()




