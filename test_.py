import sqlite3


def execute_query(*sql: str) -> list:
    for i in sql:
        with sqlite3.connect('students.db') as con:
            cur = con.cursor()
            cur.execute(i)
            return cur.fetchall()

sql1 = """
SELECT AVG(t.grade), teachers.full_name 
FROM total AS t
JOIN teachers AS teachers ON t.teacher_id = teachers.id
GROUP BY teachers.full_name
"""
print(execute_query(sql1))
print(len(execute_query(sql1)))
