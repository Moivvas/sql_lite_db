SELECT d.name, gr.name, ROUND(AVG(g.grade), 2 ) as average_grade
FROM grades g
JOIN students s ON s.id = g.student_id 
JOIN disciplines d  ON d.id = g.discipline_id 
JOIN [groups] gr ON gr.id = s.group_id 
WHERE d.id = 6
GROUP BY gr.name, d.name 
ORDER BY average_grade DESC;