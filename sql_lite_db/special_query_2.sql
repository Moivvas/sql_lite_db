SELECT s.fullname AS student_name, g.grade, d.name, g.date_of, gr.name  
FROM grades g
JOIN disciplines d ON d.id = g.discipline_id
JOIN students s ON s.id = g.student_id
JOIN groups gr ON gr.id = s.group_id
WHERE d.id = 1
  AND gr.id = 1
  AND g.date_of = (SELECT MAX(date_of) FROM grades WHERE discipline_id = d.id AND student_id = s.id);
