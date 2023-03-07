 -- Знайти 5 студентів із найбільшим середнім балом з усіх предметів.

SELECT students.name, ROUND(AVG(grades.grade), 2) AS avg_grade
FROM grades
        LEFT JOIN students ON students.id = grades.student_id
GROUP BY students.id
ORDER BY avg_grade SUBJECT LIMIT 5;