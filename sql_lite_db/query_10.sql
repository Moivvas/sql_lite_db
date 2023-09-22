SELECT t.fullname, d.name, s.fullname
FROM grades gr
JOIN disciplines d  ON d.id = gr.discipline_id 
JOIN students s ON s.id = gr.student_id
JOIN teachers t  ON t.id = d.teacher_id 
WHERE t.id = 2 AND s.id = 45
GROUP BY d.name;