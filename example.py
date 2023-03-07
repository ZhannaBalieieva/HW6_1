from datetime import datetime
from faker import Faker
from random import randint, choice
import sqlite3

fake = Faker()

NUMBER_STUDENTS = 30 
NUMBER_TEACHERS = 5  
NUMBER_GROUPS = 3
NUMBER_SUBJECTS = 5
NUMBER_GRADES = 20


def generate_fake_data(number_students, number_teachers, number_groups, number_subjects, number_grades) -> tuple():
    fake_students = []  
    fake_teachers = []  
    fake_groups = []  
    fake_subjects = []  
    fake_grades = []   

    fake_data = faker.Faker()

        
    for _ in range(number_students):
        fake_students.append(fake_data.name())
    
    for _ in range(number_teachers):
        fake_teachers.append(fake_data.name())
        
    for _ in range(number_groups):
        fake_groups.append(fake_data.number())
    
    for _ in range(number_subjects):
        fake_subjects.append(fake_data.name())   
    
    for _ in range(number_grades):
        fake_grades.append(fake_data.number())    
    
      
    return fake_students, fake_teachers, fake_groups, fake_subjects, fake_grades 



def insert_data_to_db(students, teachers, groups, subjects, grades) -> None:

    with sqlite3.connect('salary.db') as con:
        cur = con.cursor()

        sql_to_students = """INSERT INTO students(student_name)
                               VALUES (?)"""

        cur.executemany(sql_to_students, students)

        sql_to_teachers = """INSERT INTO teachers(teacher_name, subjects)
                               VALUES (?, ?)"""

        cur.executemany(sql_to_teachers, teachers)

        sql_to_grades = """INSERT INTO grades(grade_number, student_name, subject_name, date_of)
                                VALUES (?, ?, ?, ?)"""

        cur.executemany(sql_to_grades, grades)
        
        
        sql_to_groups = """INSERT INTO groups(group_number)
                                VALUES (?)"""

        cur.executemany(sql_to_groups, groups)
        
        
        sql_to_subjects = """INSERT INTO subjects(subjects_name, teacher_name)
                               VALUES (?, ?)"""

        cur.executemany(sql_to_subjects, subjects)

        con.commit()


if __name__ == "__main__":
    students, teachers, groups, subjects, grades = generate_fake_data(NUMBER_STUDENTS, NUMBER_TEACHERS, NUMBER_GROUPS, NUMBER_SUBJECTS, NUMBER_GRADES)
    insert_data_to_db(students, teachers, groups, subjects, grades)
