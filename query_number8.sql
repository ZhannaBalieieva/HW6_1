-- Знайти середній бал, який ставить певний викладач зі своїх предметів.
SELECT teachers.name, round(avg(grades.grade), 2) AS avg_grade
FROM grades
         LEFT JOIN teachers ON teachers.id = subjects.teacher_id
         LEFT JOIN subjects ON subjects.id = grades.subject_id
WHERE teachers.id = 5
GROUP BY teachers.name;


