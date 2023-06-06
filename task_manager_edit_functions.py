import sqlite3

import task_manager_add_functions
import task_manager_helper_functions
import task_manager_remove_functions

columns_in = ['name', 'date', 'time', 'time_end', 'description', 'class', 'semester']

#update, set where: 3 parameter that we can use to update any table- update-table, set-column = new_value, where-value/name
def general_update(table, column, new_value, name):
    query = f'''UPDATE {table} SET {column} = {new_value} WHERE name = ?'''
    parameters = (name,)
    task_manager_helper_functions.run_query(query, parameters)


# def calendar_update(table, column, new_value, name):
#     sometimes_calendar = ['classes', 'tasks']
#     never_calendar = ['semesters', 'class_days']
#     always_calendar = ['assignments', 'tests', 'quizzes', 'appointments']
#     # 'events'
#     #'date end'
#     columns_in = ['name', 'date', 'time', 'time_end', 'description', 'class', 'semester']
#     if table in always_calendar:
#         if column in columns_in:
#             general_update('calendar', column, new_value, name)
#     elif table == 'events':
#         if column in columns_in:
#             general_update('calendar', column, new_value, name)
#         elif column == 'date_end':
#             location = task_manager_helper_functions.find_value('location', 'events', name)
#             date = task_manager_helper_functions.find_value('date', 'events', name)
#             time = task_manager_helper_functions.find_value('time', 'events', name)
#             time_end = task_manager_helper_functions.find_value('time_end', 'events', name)
#             description = task_manager_helper_functions.find_value('description', 'events', name)
#             task_manager_remove_functions.delete('events', name)
#             task_manager_add_functions.add_event(name, location, date, time, time_end, new_value, description)
#
#     elif table == 'tasks':
#         date = task_manager_helper_functions.find_value('date', 'tasks', name)
#         if date is not None:
#             if column in columns_in:
#                 general_update('calendar', column, new_value, name)
#
#     elif table == 'classes':
#check if item is in calendar
def in_calendar(name):
    entry = task_manager_helper_functions.find_value('*', 'calendar', name)
    if entry is not None:
        return True
    else:
        return False

def check_status

def check_date

#works for tasks, appointments, quizzes, tests, assignments
def general_calendar_update(column, new_value, name):
    if column == 'status':
        if new_value == 0:
            general_update('calendar', column, new_value, name)
        else:
            if in_calendar(name) is True:
                task_manager_remove_functions.delete_entry_calendar(name)
    elif column == 'date':
        if new_value is None:
            if in_calendar(name) is True:
                task_manager_remove_functions.delete_entry_calendar(name)
        else:
            general_update('calendar', column, new_value, name)

    elif in_calendar(name) is True:
        if column in columns_in:
            general_update('calendar', column, new_value, name)


def assignment_update(column, new_value, name):
    general_update('assignments', column, new_value, name)
    if column in columns_in:
        general_update('calendar', column, new_value, name)

def events_update(column, new_value, name):
    if column == 'date_end':
        location = task_manager_helper_functions.find_value('location', 'events', name)
        date = task_manager_helper_functions.find_value('date', 'events', name)
        time = task_manager_helper_functions.find_value('time', 'events', name)
        time_end = task_manager_helper_functions.find_value('time_end', 'events', name)
        description = task_manager_helper_functions.find_value('description', 'events', name)
        task_manager_remove_functions.delete('events', name)
        task_manager_add_functions.add_event(name, location, date, time, time_end, new_value, description)
    else:
        general_update('events', column, new_value, name)
        general_calendar_update(column, new_value, name)

def semester_update(column, new_value, name):
    if column == 'date' or column == 'date_end':
        general_update('semesters', column, new_value, name)
        classes = task_manager_helper_functions.find_value('classes', 'semesters', name)
        for c in classes:
            dates = task_manager_helper_functions.find_value('dates', 'classes', c)














#
# #update value in column where table is assignments and in calendar
# def update_assignments(column, new_value, name):
#     general_update("assignments", column, new_value, name)
#     if task_manager_helper_functions.is_in_calendar(column) is True:
