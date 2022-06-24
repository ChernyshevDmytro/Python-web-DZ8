from datetime import datetime
import faker
from random import randint, choice
import sqlite3

NUMBER_STUDENTS = 30
NUMBER_GROUPS = 3
SUBJECTS = ["maths", "physics", "chemistry", "hydrodynamics", "thermodynamics"]
NAME_TEACHERS = ["Cool_teacher", "laboratory assistant", "Hell_teacher"]
MARKS = list(range (1, 11))
NUMBER_MARKS = 20

def generate_fake_data(NUMBER_STUDENTS) -> tuple(): 
    first_names = []  
    fake_data = faker.Faker('ru-RU')

    for _ in range(NUMBER_STUDENTS):
        first_names.append(fake_data.name())
    return first_names
students_names=generate_fake_data(NUMBER_STUDENTS)

def prepare_data(NUMBER_GROUPS, SUBJECTS, NAME_TEACHERS, students_names, MARKS, NUMBER_MARKS) -> tuple():
    for_grades =[]
    for i in range (1, len(MARKS)+1):
        for_grades.append((i, ))      
  
    for_groups = []    
    for j in range (1, NUMBER_GROUPS+1):
        for_groups.append((j, ))

    for_students = []
    for student in students_names: 
        for_students.append((student, randint(1, NUMBER_GROUPS)))
      
    for_subjects=[]
    for subject in SUBJECTS:
        for_subjects.append((subject, ))

    for_teachers=[]
    for name in NAME_TEACHERS:
        for_teachers.append((name, ))
   
    for_all = []

    for mark in range(1, NUMBER_MARKS + 1):
        for subject in  SUBJECTS:           
            for id, student in enumerate(students_names):
                mark_date = datetime(2022, randint(1, 12), randint(10, 20)).date()
                # Выполняем цикл по количеству сотрудников
                for_all.append((id+1, student, choice(NAME_TEACHERS), subject, choice(MARKS), mark_date))

    return for_grades, for_groups, for_students, for_subjects, for_teachers, for_all

for_grades, for_groups, for_students, for_subjects, for_teachers, for_all = prepare_data(NUMBER_GROUPS, SUBJECTS, NAME_TEACHERS, students_names, MARKS, NUMBER_MARKS)

def insert_data_to_db(for_grades, for_groups, for_students, for_subjects, for_teachers, for_all) -> None:

    with sqlite3.connect('students.db') as con:

        cur = con.cursor()

        sql_to_grades = """INSERT INTO list_of_grades(grade)
                               VALUES (?)"""
        cur.executemany(sql_to_grades, for_grades)

        sql_to_groups = """INSERT INTO list_of_groups(group_number)
                               VALUES (?)"""
        cur.executemany(sql_to_groups, for_groups)


        sql_to_students = """INSERT INTO list_of_students(student_name, group_number)
                               VALUES (?, ?)"""
        cur.executemany(sql_to_students, for_students)

        sql_to_subjects = """INSERT INTO list_of_subjects(subject_name)
                              VALUES (?)"""
        cur.executemany(sql_to_subjects, for_subjects) 

        sql_to_teachers = """INSERT INTO list_of_teachers(teacher_name)
                              VALUES (?)"""
        cur.executemany(sql_to_teachers, for_teachers)


        sql_to_all = """INSERT INTO total(student_id, student_name, teacher_name, subject_name, grade, graded_at)
                              VALUES (?, ?, ?, ?, ?, ?)"""
        cur.executemany(sql_to_all, for_all)

        con.commit()
if __name__ == "__main__":
    insert_data_to_db(for_grades, for_groups, for_students, for_subjects, for_teachers, for_all)  