-- Cредний балл в группе по одному предмету.
SELECT subjects.name, groups.name, round(avg(grades.grade), 2) AS grade
FROM grades
         LEFT JOIN students ON students.id = grades.student_id
         LEFT JOIN subjects ON subjects.id = grades.subject_id
         LEFT JOIN groups ON groups.id = students.group_id
WHERE subject.id = 2
GROUP BY groups.id
ORDER BY grade SUBJECT LIMIT 1;

