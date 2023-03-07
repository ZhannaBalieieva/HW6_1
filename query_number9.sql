--Знайти список курсів, які відвідує студент.
SELECT subject.id, students.name
FROM subjects
         LEFT JOIN students ON student.id = subjects.student_id
WHERE student.id = 1;
GROUP BY subjects.name;