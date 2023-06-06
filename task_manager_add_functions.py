import sqlite3
import task_manager_helper_functions
#import datetime module to use in the find class date
from datetime import datetime, timedelta

#adds an entry to the calendar where all the information will be added
def add_entry_calendar(name, date, time = None, time_end = None, description = None, class_name = None, semester = None):
    query = '''INSERT INTO calendar (name, date, time, time_end, description, class, semester) VALUES (?,?,?,?,?,?,?)'''
    parameters = (name, date, time, time_end, description, class_name, semester)
    task_manager_helper_functions.run_query(query, parameters)

#adds a semester to the semesters table
def add_semester(name, date, date_end, classes = None):
    query = '''INSERT INTO semesters (name, date, date_end, classes) VALUES (?,?,?,?)'''
    parameters = (name, date, date_end, classes)
    task_manager_helper_functions.run_query(query, parameters)


#adds a class to the classes table and to the semesters table
def add_class( name, time, time_end, location, type, professor, semester, description = None, dates = None):
    query = '''INSERT INTO classes ( name, time, time_end, dates, location, type, professor, semester, description) VALUES (?,?,?,?,?,?,?,?,?)'''
    parameters = (name, time, time_end, dates, location, type, professor, semester, description)
    task_manager_helper_functions.run_query(query, parameters)
    task_manager_helper_functions.add_class_semester(name, semester)




#adds the dates of each class- also adds to the calendar
def add_class_dates(class_name, sunday, monday, tuesday, wednesday, thursday, friday, saturday):
    class_row = task_manager_helper_functions.find_class_row(class_name)
    semester = task_manager_helper_functions.find_semester(class_row)
    semester_row = task_manager_helper_functions.find_semester_row(semester)
    begin_date = task_manager_helper_functions.find_begin_date(semester_row)
    end_date = task_manager_helper_functions.find_end_date(semester_row)
    days_included = task_manager_helper_functions.find_days_included(sunday, monday, tuesday, wednesday, thursday, friday, saturday)
    class_dates = task_manager_helper_functions.find_dates(begin_date, end_date, days_included)
    begin_time = task_manager_helper_functions.find_begin_time(class_row)
    end_time = task_manager_helper_functions.find_end_time(class_row)
    description = task_manager_helper_functions.find_description(class_row)
    task_manager_helper_functions.add_dates_calendar(class_name,class_dates,begin_time,end_time, semester, description)
    task_manager_helper_functions.add_dates_class(class_name, class_dates)

#add assignment for a class and to the calendar
def add_assignment(name, class_name , date, time, priority, description = None, status = 0):
    class_row = task_manager_helper_functions.find_class_row(class_name)
    semester = task_manager_helper_functions.find_semester(class_row)
    query = "INSERT INTO assignments(name, class, date, time, priority, description, status) VALUES (?,?,?,?,?,?,?)"
    parameters = (name, class_name, date, time, priority, description, status)
    task_manager_helper_functions.run_query(query, parameters)

    if status == 0:
        add_entry_calendar(name,date,None,time,description, class_name, semester)

#add test to tests table and to the calendar
def add_test(name, class_name , date, time,time_end, location, description = None):
    class_row = task_manager_helper_functions.find_class_row(class_name)
    semester = task_manager_helper_functions.find_semester(class_row)
    query = "INSERT INTO tests(name, class, date, time, time_end, description, location) VALUES (?,?,?,?,?,?,?)"
    parameters = (name, class_name, date, time, time_end, description, location)
    task_manager_helper_functions.run_query(query, parameters)
    add_entry_calendar(name,date,time,time_end,description, class_name, semester)


# add quiz to quizzes table and to the calendar
def add_quiz(name, class_name, date, time, time_end, status, location, description=None):
    class_row = task_manager_helper_functions.find_class_row(class_name)
    semester = task_manager_helper_functions.find_semester(class_row)
    query = "INSERT INTO quizzes(name, class, date, time, time_end, description, status, location) VALUES (?,?,?,?,?,?,?,?)"
    parameters = (name, class_name, date, time, time_end, description,status, location)
    task_manager_helper_functions.run_query(query, parameters)
    add_entry_calendar(name, date, time, time_end, description, class_name, semester)

#add appointment to appointments table and to the calendar
def add_appointment(name, location, date, time, time_end, description=None):
    query = "INSERT INTO appointments(name, location, date, time, time_end, description) VALUES (?,?,?,?,?,?)"
    parameters = (name, location, date, time, time_end, description)
    task_manager_helper_functions.run_query(query, parameters)
    add_entry_calendar(name, date, time, time_end, description, None)

#add task to tasks table and to the calendar
def add_task(name,priority, time ,status, date = None, description=None):
    query = "INSERT INTO tasks(name, priority, date, time,status, description) VALUES (?,?,?,?,?,?)"
    parameters = (name, priority, date, time, status, description)
    task_manager_helper_functions.run_query(query, parameters)
    if date is not None and status == 0:
        add_entry_calendar(name, date, None, time, description, None, None)

#add event to events table and to the calendar
def add_event(name, location, date, time, time_end, date_end = None, description=None):
    query = "INSERT INTO events(name, location, date, date_end, time, time_end, description) VALUES (?,?,?,?,?,?,?)"
    parameters = (name, location, date, date_end, time, time_end, description)
    task_manager_helper_functions.run_query(query, parameters)
    if date_end is None:
        add_entry_calendar(name, date, time, time_end, description)
    else:
        begin_date_dt = datetime.strptime(date, '%Y-%m-%d')
        end_date_dt = datetime.strptime(date_end, '%Y-%m-%d')

        # create an iterator date to go from begin to end date
        current_date = begin_date_dt
        # iterate through all the dates and add them individually to calendar
        while current_date <= end_date_dt:
            add_entry_calendar(name, current_date, time, time_end, description)
            # move on to next day
            current_date += timedelta(days=1)

