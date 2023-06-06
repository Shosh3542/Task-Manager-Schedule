import sqlite3
import task_manager_helper_functions
import task_manager_add_functions
import task_manager_remove_functions

#
task_manager_helper_functions.print_table('tasks')
task_manager_helper_functions.print_table('appointments')
task_manager_helper_functions.print_table('events')
task_manager_helper_functions.print_table('tests')
task_manager_helper_functions.print_table('quizzes')
task_manager_helper_functions.print_table('assignments')
task_manager_helper_functions.print_table('classes')
task_manager_helper_functions.print_table('semesters')
task_manager_helper_functions.print_table('class_days')
task_manager_helper_functions.print_table('calendar')

task_manager_add_functions.add_semester('Spring Semester', '2023-01-27', '2023-05-10')
task_manager_add_functions.add_semester('Fall Semester', '2023-09-01', '2024-01-10', None)
task_manager_add_functions.add_class('Chemistry', '04:00', '06:00', 'Lovener ', 'Lab', 'Mr.Peloso', 'Fall Semester')
task_manager_add_functions.add_class('Chemistry Lab', '04:00', '06:00', 'Lovener ', 'Lab', 'Mr.Peloso', 'Spring Semester')
task_manager_add_functions.add_class_dates('Chemistry',0,0,1,0,1,0,0)
task_manager_add_functions.add_class_dates('Chemistry Lab',0,1,0,1,0,0,0)
task_manager_add_functions.add_assignment('Homework 1', 'Chemistry', '2023-07-13', '11:59', 3, 'Very Hard')
task_manager_add_functions.add_assignment('Homework 2', 'Chemistry Lab', '2023-11-13', '03:05', 2,None, 1)
task_manager_add_functions.add_quiz('Quiz 1', 'Chemistry', '2023-05-13', '3:00', '4:00', 0, 'Online', 'Super Hard')
task_manager_add_functions.add_quiz('Quiz 3', 'Chemistry Lab', '2023-06-13', '4:00', '4:05', 1, 'Lovener Hall')
task_manager_add_functions.add_test('Midterm', 'Chemistry', '2023-11-21', '11:00', '01:00', 'Online', 'Study Alot')
task_manager_add_functions.add_test('Midterm 2', 'Chemistry Lab', '2023-12-23', '12:00', '03:00', 'Lovener Hall')
task_manager_add_functions.add_task('Play Piano', 3, '12:20',0, '2023-07-03', 'Play for 1 hour')
task_manager_add_functions.add_task('Go grocery shopping', 2, '3:00', 0)
task_manager_add_functions.add_appointment('Therapy', '248 Oakwood Ave', '2023-08-13', '01:30', '03:40', 'for foot issue')
task_manager_add_functions.add_appointment('Doctor', '238 Oakwood Ave', '2023-07-13', '01:40', '05:40')
task_manager_add_functions.add_event('Concert', 'NYC', '2023-11-03', '03:00', '05:00', '2023-11-06', 'Taylor Swift')
task_manager_add_functions.add_event('Art Show', '333 Random Road', '2023-09-13', '11:00','12:00' )

task_manager_helper_functions.print_table('tasks')
task_manager_helper_functions.print_table('appointments')
task_manager_helper_functions.print_table('events')
task_manager_helper_functions.print_table('tests')
task_manager_helper_functions.print_table('quizzes')
task_manager_helper_functions.print_table('assignments')
task_manager_helper_functions.print_table('classes')
task_manager_helper_functions.print_table('semesters')
task_manager_helper_functions.print_table('class_days')
task_manager_helper_functions.print_table('calendar')

task_manager_remove_functions.delete('tasks', 'Play Piano')
task_manager_remove_functions.delete('appointments', 'Therapy')
task_manager_remove_functions.delete('events', 'Concert')
task_manager_remove_functions.delete('tests', 'Midterm 2')
task_manager_remove_functions.delete('quizzes', 'Quiz 3')
task_manager_remove_functions.delete('assignments', 'Homework 2')

task_manager_helper_functions.print_table('tasks')
task_manager_helper_functions.print_table('appointments')
task_manager_helper_functions.print_table('events')
task_manager_helper_functions.print_table('tests')
task_manager_helper_functions.print_table('quizzes')
task_manager_helper_functions.print_table('assignments')
task_manager_helper_functions.print_table('classes')
task_manager_helper_functions.print_table('semesters')
task_manager_helper_functions.print_table('class_days')
task_manager_helper_functions.print_table('calendar')

task_manager_remove_functions.delete_semester('Fall Semester')

task_manager_helper_functions.print_table('tasks')
task_manager_helper_functions.print_table('appointments')
task_manager_helper_functions.print_table('events')
task_manager_helper_functions.print_table('tests')
task_manager_helper_functions.print_table('quizzes')
task_manager_helper_functions.print_table('assignments')
task_manager_helper_functions.print_table('classes')
task_manager_helper_functions.print_table('semesters')
task_manager_helper_functions.print_table('class_days')
task_manager_helper_functions.print_table('calendar')

task_manager_remove_functions.delete_semester('Spring Semester')
task_manager_remove_functions.delete('tasks', 'Go grocery shopping')
task_manager_remove_functions.delete('appointments', 'Doctor')
task_manager_remove_functions.delete('events', 'Art Show')


task_manager_helper_functions.print_table('tasks')
task_manager_helper_functions.print_table('appointments')
task_manager_helper_functions.print_table('events')
task_manager_helper_functions.print_table('tests')
task_manager_helper_functions.print_table('quizzes')
task_manager_helper_functions.print_table('assignments')
task_manager_helper_functions.print_table('classes')
task_manager_helper_functions.print_table('semesters')
task_manager_helper_functions.print_table('class_days')
task_manager_helper_functions.print_table('calendar')



















