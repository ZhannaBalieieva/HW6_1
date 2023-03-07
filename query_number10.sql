-- Список курсів, які певному студенту читає певний викладач.
SELECT students.name, teachers.name, subjects.name
FROM grades
         LEFT JOIN students ON students.id = grades.student_id
         LEFT JOIN subjects ON subject.id = grades.subject_id
         LEFT JOIN teachers ON teachers.id = subjects.teacher_id
WHERE grades.student_id = 1
  AND teachers.id = 2
GROUP BY subject.name;