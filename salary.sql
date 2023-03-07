BEGIN TRANSACTION;

DROP TABLE IF EXISTS students;
CREATE TABLE students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name student_name UNIQUE NOT NULL,
    group_id REFERENCES groups (id)
);

DROP TABLE IF EXISTS teachers;
CREATE TABLE teachers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name STRING UNIQUE NOT NULL
);

DROP TABLE IF EXISTS groups;
CREATE TABLE groups (
    id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
    name STRING UNIQUE
);


-- Table: subjects where teacher read a subjects
DROP TABLE IF EXISTS subjects;
CREATE TABLE subjects (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name STRING UNIQUE NOT NULL,
    teacher_id REFERENCES teachers (id)
);


-- Table: subjects where teacher read a subjects
DROP TABLE IF EXISTS grades;
CREATE TABLE grades (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id REFERENCES students (id),
    date_of DATE NOT NULL,
    subject_id REFERENCES subjects (id),
    rates INTEGER NOT NULL
);


COMMIT TRANSACTION;
