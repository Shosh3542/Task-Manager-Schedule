import sqlite3
import task_manager_helper_functions

#deletes a calendar entry
def delete_entry_calendar(name):
    query = '''DELETE FROM calendar WHERE name = ?'''
    parameters = (name, )
    task_manager_helper_functions.run_query(query, parameters)

#general delete function we use for all delete functions
def delete(table, name, is_c_or_s = False, column = None):
    if is_c_or_s == False:
        delete_entry_calendar(name)
        query = f'''DELETE FROM {table} WHERE name = ?'''
        parameters = (name, )
        task_manager_helper_functions.run_query(query, parameters)
    else:
        query = f'''DELETE FROM {table} WHERE {column} = ?'''
        parameters = (name, )
        task_manager_helper_functions.run_query(query, parameters)



#deletes a class and its associated assignments, tests, quizzes, and removes it from the calendar(and all of them) and semester
def delete_class(name, semester):
    delete('calendar', name, True, 'class')
    delete('assignments', name, True,'class')
    delete('quizzes', name, True, 'class')
    delete('tests', name, True, 'class')
    delete('classes', name)
    task_manager_helper_functions.remove_class_semester(name, semester)

#make sure you comma seperate the classes in semesters

#deletes a semester from the semesters table and associated classes and dates
def delete_semester(name, classes = None):
    query1 = 'SELECT classes FROM semesters WHERE name = ?'
    parameters1 = (name, )
    classes = task_manager_helper_functions.find_item(query1, parameters1)
    print(classes)
    if classes != None:
        for c in classes:
         print('Class to remove: ' + c)
         delete_class(c, name)
    delete('semesters',name )
    delete('calendar', name, True, 'semester')

    # #deletes a quiz from the quizzes table and the calendar
    # def delete_quiz(name):
    #     delete_entry_calendar(name)
    #     query = '''DELETE FROM quizzes WHERE name = ?'''
    #     parameters = (name, )
    #     task_manager_helper_functions.run_query(query, parameters)

    # #deletes a test from the tests table and the calendar
    # def delete_test(name):
    #     delete_entry_calendar(name)
    #     query = '''DELETE FROM tests WHERE name = ?'''
    #     parameters = (name, )
    #     task_manager_helper_functions.run_query(query, parameters)

    # #deletes an assignment from the assignments table and the calendar
    # def delete_assignment(name):
    #     delete_entry_calendar(name)
    #     query = '''DELETE FROM assignments WHERE name = ?'''
    #     parameters = (name, )
    #     task_manager_helper_functions.run_query(query, parameters)

    # #deletes a task from the tasks table and the calendar
    # def delete_task(name):
    #     delete_entry_calendar(name)
    #     query = '''DELETE FROM tasks WHERE name = ?'''
    #     parameters = (name, )
    #     task_manager_helper_functions.run_query(query, parameters)

    # #deletes an appointment from the appointments table and the calendar
    # def delete_appointment(name):
    #     delete_entry_calendar(name)
    #     query = '''DELETE FROM appointments WHERE name = ?'''
    #     parameters = (name, )
    #     task_manager_helper_functions.run_query(query, parameters)

    # #deletes an event from the events table and the calendar
    # def delete_event(name):
    #     delete_entry_calendar(name)
    #     query = '''DELETE FROM events WHERE name = ?'''
    #     parameters = (name, )
    #     task_manager_helper_functions.run_query(query, parameters)




