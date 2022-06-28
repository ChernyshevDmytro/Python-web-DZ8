import sqlite3


def execute_query(*sql: str) -> list:
    for i in sql:
        with sqlite3.connect('students.db') as con:
            cur = con.cursor()
            cur.execute(i)
            return cur.fetchall()

sql1 = """
SELECT AVG(t.grade), students.full_name 
FROM total AS t
JOIN students AS students ON t.student_id = students.id
GROUP BY t.student_id
ORDER BY AVG(t.grade) DESC
LIMIT 5
"""

sql2 = """
SELECT AVG(t.grade), students.full_name, subjects.subject
FROM total AS t
JOIN students AS students ON t.student_id = students.id
JOIN subjects AS subjects ON t.subject_id = subjects.id
GROUP BY t.student_id, t.subject_id
ORDER BY AVG(t.grade) DESC
LIMIT 1
"""

sql3 = """
SELECT students_in_group.group_id, AVG(t.grade), subjects.subject
FROM total AS t
JOIN students_in_group AS students_in_group ON students_in_group.student_id = t.student_id
JOIN subjects AS subjects ON t.subject_id = subjects.id
GROUP BY students_in_group.group_id, subjects.id
ORDER BY students_in_group.group_id ASC
LIMIT 15
"""

sql4 = """
SELECT AVG (grade) 
FROM total
"""

sql5 = """
SELECT teachers.full_name, subjects.subject
FROM total AS t
JOIN teachers AS teachers ON teachers.id = t.teacher_id
JOIN subjects AS subjects ON t.subject_id = subjects.id
GROUP BY teachers.id, subjects.id
ORDER BY teachers.id ASC
"""

sql6 = """
SELECT students.full_name, students_in_group.group_id
FROM students AS students
JOIN students_in_group AS students_in_group ON students_in_group.student_id = students.id
ORDER BY students_in_group.group_id
"""
sql7 = """
SELECT s.full_name, students_in_group.group_id, subjects.subject, t.grade
FROM total AS t
JOIN students AS s ON s.id = t.student_id
JOIN students_in_group AS students_in_group ON students_in_group.student_id = t.student_id
JOIN subjects AS subjects ON subjects.id = t.student_id
WHERE subjects.id = 1 AND students_in_group.group_id =1
ORDER BY subjects.id, students_in_group.group_id
"""

sql8 = """
SELECT students.full_name, subjects.subject, t.grade
FROM total AS t
JOIN students_in_group AS students_in_group ON t.student_id = students_in_group.student_id 
JOIN students AS students ON t.student_id = students.id 
JOIN subjects AS subjects ON subjects.id = t.subject_id 
WHERE students_in_group.group_id = 1
ORDER BY t.graded_at DESC LIMIT 50
"""

sql9 = """
SELECT students.full_name, subjects.subject
FROM total as t
JOIN subjects AS subjects ON subjects.id = t.subject_id 
JOIN students AS students ON t.student_id = students.id 
WHERE t.student_id = 1
GROUP BY students.full_name, subjects.subject
"""
sql10 = """
SELECT students.full_name, subjects.subject, teachers.full_name
FROM total as t
JOIN subjects AS subjects ON subjects.id = t.subject_id 
JOIN students AS students ON t.student_id = students.id 
JOIN teachers AS teachers ON teachers.id = t.teacher_id
WHERE t.student_id = 1
GROUP BY students.full_name, subjects.subject
"""

sql11 = """
SELECT AVG(grade) 
FROM total 
"""
sql12 = """
SELECT AVG(t.grade), teachers.full_name 
FROM total AS t
JOIN teachers AS teachers ON t.teacher_id = teachers.id
GROUP BY teachers.full_name
"""

sqls=[sql1, sql2, sql3, sql4, sql5, sql6, sql7, sql8, sql9, sql10, sql11, sql12]

for i in sqls:
    print(execute_query(i))

"""WHERE LIMIT 5
"""