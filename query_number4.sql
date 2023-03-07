-- Знайти середній бал на потоці (по всій таблиці оцінок).

SELECT round(avg(grade),2) AS avg_grade
FROM grades;