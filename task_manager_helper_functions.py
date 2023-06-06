import sqlite3
#import datetime module to use in the find class date
from datetime import datetime, timedelta

import task_manager_add_functions
import pandas as pd

#helper method to create connection to database
def create_connection():
    con = sqlite3.connect('task_manager.db')
    return con

#commits data and closes the database
def close_connection(con):
    con.commit()
    con.close()

#runs the given query and parameters
def run_query( query, parameters = None):
    con = create_connection()
    c = con.cursor()
    c.execute(query, parameters)
    close_connection(con)

#use this for the class_dates and begin_date and end_date function
def find_item( query, parameters = None):
    con = create_connection()
    c = con.cursor()
    c.execute(query, parameters)
    result = c.fetchone()
    close_connection(con)
    return result

#return the table
def return_table(query):
    con = create_connection()
    c = con.cursor()
    c.execute(query)
    result = c.fetchall()
    close_connection(con)
    return result

#print the table
def print_table2(result):
    for row in result:
        print(result)

#use pandas to print the entire table
def print_table(table_name):
    # Connect to the SQLite database
    con = create_connection()

    # Define SQL query
    query = f"SELECT * FROM {table_name}"

    # Use pandas to execute the query and fetch data
    df = pd.read_sql_query(query, con)

    # Print the dataframe
    print(df)

    # Close the connection
    close_connection(con)

#finds the specified row of the class table
def find_class_row(class_name):
    query = "SELECT * FROM classes WHERE name = ?"
    parameter = (class_name, )
    row_needed = find_item(query,parameter)
    return row_needed

#finds the semester of the specified class
def find_semester(class_row):
    if class_row is not None:
        semester_needed = class_row[7] #position of the semester column in the classes table
        return semester_needed

#find the specified row of the semester table
def find_semester_row(semester):
    query = "SELECT * FROM semesters WHERE name = ?"
    parameter = (semester, )
    row_needed = find_item(query,parameter)
    return row_needed

def find_classes_semester(semester_row):
    if semester_row is not None:
        if semester_row[3] is not None:
            return semester_row[3]



#update the semester by adding the class
def add_class_semester(name, semester):
    print(f'Adding class: {name} to semester: {semester}')  # For debugging
    current_classes = find_classes_semester(find_semester_row(semester))
    print(f'Current classes: {current_classes}')  # For debugging

    if current_classes is not None:
        all_classes = current_classes + "," + name
    else:
        all_classes = name

    print(f'All classes after addition: {all_classes}')  # For debugging

    query = "UPDATE semesters SET classes = ? WHERE name = ?"
    parameters = (all_classes, semester)
    run_query(query, parameters)

#update the semester by removing a class
def remove_class_semester(name, semester):
    #get current classes
    current_classes = find_classes_semester(find_semester_row(semester))
    print(f'Current classes: {current_classes}')  # For debugging
    print(f'Class to remove: {name}')  # For debugging

    if current_classes:
    #remove class from classes
        current_classes_list = current_classes.split(',')

    try:
        current_classes_list.remove(name)

    except ValueError:
        pass
    #convert back to string
    all_classes = ",".join(current_classes_list)

    #update the database
    query = "UPDATE semesters SET classes = ? WHERE name = ?"
    parameters = (all_classes, semester)
    run_query(query, parameters)

#finds the begin date of the semester
def find_begin_date(semester_row):
    if semester_row is not None:
        begin_date = semester_row[1]
        return begin_date


#finds the end date of the semester
def find_end_date(semester_row):
    if semester_row is not None:
        end_date = semester_row[2]
        return end_date

#finds the begin time of a class
def find_begin_time(class_row):
    if class_row is not None:
        begin_time = class_row[1]
        return begin_time

#finds the end time of a class
def find_end_time(class_row):
    if class_row is not None:
        end_time = class_row[2]
        return end_time

#find the description of a class
def find_description(class_row):
    if class_row is not None:
        if class_row[8] is not None:
            return class_row[8]

#creates a list of which days of the week the class takes place
def find_days_included(sunday, monday, tuesday, wednesday, thursday, friday, saturday):
    # create list to add days of the week included in class
    days_included = []
    # add all the selected days to the days included list
    if sunday == 1:
        days_included.append(6)
    if monday == 1:
        days_included.append(0)
    if tuesday == 1:
        days_included.append(1)
    if wednesday == 1:
        days_included.append(2)
    if thursday == 1:
        days_included.append(3)
    if friday == 1:
        days_included.append(4)
    if saturday == 1:
        days_included.append(5)
    return days_included

#iterate through the dates and return list of all included dates
def find_dates(date, date_end, days_included):
    #convert begin and end dates to their datetime equivalents
    begin_date_dt = datetime.strptime(date, '%Y-%m-%d')
    end_date_dt = datetime.strptime(date_end, '%Y-%m-%d')

    #create a list to hold the dates for each class
    class_dates = []

    #create an iterator date to go from begin to end date
    current_date = begin_date_dt
    #iterate through all the dates and add to class_dates if days match list
    while current_date <= end_date_dt:
        if current_date.weekday() in days_included:
            class_dates.append(current_date)

        #move on to next day
        current_date += timedelta(days = 1)
    #return class_dates list
    return class_dates

#add the dates to the calendar
def add_dates_calendar(name, class_dates, time, time_end, semester, description = None ):
    for date in class_dates:
        task_manager_add_functions.add_entry_calendar(name, date, time, time_end, description, name, semester)

#add the dates to the class
def add_dates_class(class_name, class_dates):
    class_dates_str = str(class_dates)
    query = "UPDATE classes SET dates = ? WHERE name = ?"
    parameters = (class_dates_str, class_name)
    run_query(query, parameters)

#check if the column is in the calendar
def is_in_calendar(column):
    query = '''SELECT '''
    if column == "name" or column == "date" or column == "time" or column == "time_end" or column == "description" or column == "class":
        return True
    else:
        return False

def find_value(column, table, name):
    query = f'''SELECT {column} FROM {table} WHERE name = ?'''
    parameters = (name, )
    value = find_item(query, parameters)
    return value

























