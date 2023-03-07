from datetime import date, datetime, timedelta
from random import randint
import sqlite3
import os
import faker

def create_db():
    # читаємо файл зі скриптом для створення БД
    
    with open('salary.sql', 'r') as f:
        sql = f.read()

    # створюємо з'єднання з БД (якщо файлу з БД немає, він буде створений)
    with sqlite3.connect('salary.db') as conn:
        cur = conn.cursor()
        # виконуємо скрипт із файлу, який створить таблиці в БД
        cur.executescript(sql)
        conn.commit()

#students, teachers, groups, subjects, rates

def fill_data():
    # Не всі данні будуть динамічні, заповнюєм статичні
    subjects = ['Вища математика', 'Хімія', 'Економіка підприємства', 'Обчислювальна математика', 'Історія України',
                   'Теоретична механіка', 'Менеджмент організацій', 'Системне програмування']

    groups = ['ВВ1', 'ДД33', 'АА5']

    fake = faker.Faker('uk-UA')
    conn = sqlite3.connect('salary.db')
    cur = conn.cursor()
    number_of_teachers = 5
    number_of_students = 30

############  students, teachers, groups, subjects, rates

    def seed_teachers():
        teachers = []

        for _ in range(number_of_teachers):
            teachers.append(fake.name())
        sql_teachers = 'INSERT INTO teachers(name) VALUES (?)'
        # https://docs.python.org/3/library/sqlite3.html#sqlite3.Cursor.executemany
        cur.executemany(sql_teachers, zip(teachers, ))

    def seed_subjects():
        sql_subjects = 'INSERT INTO subjects(name, teacher_id) VALUES (?, ?)'
        cur.executemany(
            sql_subjects,
            zip(
                subjects, iter(randint(1, number_of_teachers) for _ in range(len(subjects)))
            )
        )

    def seed_groups():
        sql_groups = 'INSERT INTO groups(name) VALUES (?)'
        cur.executemany(sql_groups, zip(groups, ))

    def seed_students():
        students = []
        for _ in range(number_of_students):
            students.append(fake.name())
        sql_students = 'INSERT INTO students(name, group_id) VALUES (?,?)'
        cur.executemany(sql_students, zip(students, iter(randint(1, len(groups)) for _ in range(len(students)))))

    def seed_grades():
        # дата початку навчального року
        start_date = datetime.strptime("2022-09-01", "%Y-%m-%d")
        # дата кінця навчального року
        end_date = datetime.strptime("2023-05-25", "%Y-%m-%d")
        d_range = date_range(start=start_date, end=end_date)

        grades = []

        for d in d_range:
            # Випадково берем id дисципліни. Вважаєм, що в один день - один предмет
            r_subjects = randint(1, len(subjects))
            # припустимо, що в один день можуть відповісти 3 студента
            # обираємо 3-ох з 30-ти
            r_students = [randint(1, number_of_students) for _ in range(3)]
            for student in r_students:
                grades.append((student, r_subjects, d.date(), randint(1, 12)))
        sql_ratings = 'INSERT INTO grades(student_id, subject_id, date_of, grade) VALUES (?, ?, ?, ?)'
        cur.executemany(sql_ratings, grades)

    try:
        seed_teachers()
        seed_subjects()
        seed_groups()
        seed_students()
        seed_grades()
        conn.commit()

    except sqlite3.IntegrityError as err:
        print(err)

    finally:
        conn.close()


if __name__ == '__main__':
    create_db('salary.sql')
    fill_data()

