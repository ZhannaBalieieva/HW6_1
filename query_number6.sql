---- Знайти список студентів у певній групі.
SELECT student.id, students.name, groups.name
FROM students
         LEFT JOIN groups ON groups.id = students.group_id
WHERE groups.id = 1;

