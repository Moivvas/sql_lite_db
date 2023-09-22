SELECT g.name, d.name, gr.grade
FROM students s
JOIN groups g ON g.id = s.group_id 
JOIN grades gr ON gr.student_id = s.id
JOIN disciplines d ON d.id = gr.discipline_id
WHERE g.id = 2 AND d.id =2;