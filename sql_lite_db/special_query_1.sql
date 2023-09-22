SELECT t.fullname, ROUND(AVG(g.grade), 2) as average_grade, s.fullname
FROM grades g
JOIN disciplines d  ON d.id = g.discipline_id 
JOIN students s ON s.id = g.student_id
JOIN teachers t  ON t.id = d.teacher_id 
WHERE t.id = 1 AND s.id = 22
GROUP BY t.fullname, s.fullname;