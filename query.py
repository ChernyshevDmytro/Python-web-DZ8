import sqlite3


def execute_query(*sql: str) -> list:
    for i in sql:
        with sqlite3.connect('students.db') as con:
            cur = con.cursor()
            cur.execute(i)
            return cur.fetchall()

sql1 = """
SELECT AVG(t.grade), t.student_name 
FROM total AS t
JOIN list_of_students AS students ON t.student_name = students.student_name 
GROUP BY t.student_name
LIMIT 5
"""

sql2 = """
SELECT AVG(t.grade), t.student_name, t.subject_name 
FROM total AS t
LEFT JOIN list_of_students AS students ON t.student_name = students.student_name 
GROUP BY t.subject_name
"""

sql3 = """
SELECT AVG(t.grade) 
FROM total AS t
LEFT JOIN list_of_students AS groups ON t.student_name = groups.student_name
GROUP BY groups.group_number
"""

sql4 = """
SELECT AVG (grade) 
FROM total
"""

sql5 = """
SELECT teacher_name, subject_name 
FROM total
GROUP BY teacher_name, subject_name
"""

sql6 = """
SELECT student_name, group_number 
FROM list_of_students
ORDER BY group_number
"""
sql7 = """
SELECT t.student_name, s.group_number, t.subject_name, t.grade 
FROM total AS t
JOIN list_of_students AS s ON t.student_name = s.student_name
ORDER BY s.group_number, t.student_name
"""

sql8 = """
SELECT t.student_name, s.group_number, t.subject_name, t.grade
FROM total AS t
JOIN list_of_students AS s ON t.student_name = s.student_name
ORDER BY  t.graded_at DESC LIMIT 30
"""

sql9 = """
SELECT student_name, subject_name 
FROM total
GROUP BY student_name, subject_name
"""
sql10 = """
SELECT student_name, subject_name, teacher_name 
FROM total
GROUP BY student_name, teacher_name
"""

sql11 = """
SELECT AVG(t.grade), t.student_name, teachers.teacher_name 
FROM total AS t
LEFT JOIN list_of_teachers AS teachers ON t.teacher_name = teachers.teacher_name
"""
sql12 = """
SELECT AVG(t.grade), teachers.teacher_name 
FROM total AS t
JOIN list_of_teachers AS teachers ON t.teacher_name = teachers.teacher_name
GROUP BY teachers.teacher_name
"""

sqls=[sql1, sql2, sql3, sql4, sql5, sql6, sql7, sql8, sql9, sql10, sql11, sql12]

for i in sqls:
    print(execute_query(i))

"""WHERE LIMIT 5
"""