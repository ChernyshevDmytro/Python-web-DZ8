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
  
    for_groups = []    
    for j in range (1, NUMBER_GROUPS+1):
        for_groups.append((j, ))

    for_students = []
    for student in students_names: 
        for_students.append((student, ))

    for_students_in_group = []
    for id, student in enumerate(students_names):
        if id <=10:
            group_number=1
        elif id >10 and id <=20:
            group_number=2
        else:
            group_number=3  
        for_students_in_group.append((id+1, group_number, ))        
      
    for_subjects=[]
    for subject in SUBJECTS:
        for_subjects.append((subject, ))

    for_teachers=[]
    for name in NAME_TEACHERS:
        for_teachers.append((name, ))
   
    for_all = []

    for mark in range(1, NUMBER_MARKS + 1):
        for subject in range(1, len(SUBJECTS)+1):           
            for id in range(1, len(students_names)+1):                            
                mark_date = datetime(2022, randint(1, 12), randint(10, 20)).date()                
                for_all.append((id, choice(range(1, len(NAME_TEACHERS)+1)), subject, choice(MARKS), mark_date))

    return for_groups, for_students, for_students_in_group, for_subjects, for_teachers, for_all

for_groups, for_students, for_students_in_group, for_subjects, for_teachers, for_all = prepare_data(NUMBER_GROUPS, SUBJECTS, NAME_TEACHERS, students_names, MARKS, NUMBER_MARKS)

def insert_data_to_db(for_groups, for_students, for_students_in_group, for_subjects, for_teachers, for_all) -> None:

    with sqlite3.connect('students.db') as con:

        cur = con.cursor()

        sql_to_groups = """INSERT INTO groups(number)
                               VALUES (?)"""
        cur.executemany(sql_to_groups, for_groups)


        sql_to_students = """INSERT INTO students(full_name)
                               VALUES (?)"""
        cur.executemany(sql_to_students, for_students)

        sql_to_students_in_groups = """INSERT INTO students_in_group(student_id, group_id)
                               VALUES (?, ?)"""
        cur.executemany(sql_to_students_in_groups, for_students_in_group)


        sql_to_subjects = """INSERT INTO subjects(subject)
                              VALUES (?)"""
        cur.executemany(sql_to_subjects, for_subjects) 

        sql_to_teachers = """INSERT INTO teachers(full_name)
                              VALUES (?)"""
        cur.executemany(sql_to_teachers, for_teachers)


        sql_to_all = """INSERT INTO total(student_id, teacher_id, subject_id, grade, graded_at)
                              VALUES (?, ?, ?, ?, ?)"""
        cur.executemany(sql_to_all, for_all)

        con.commit()
if __name__ == "__main__":
    insert_data_to_db(for_groups, for_students, for_students_in_group, for_subjects, for_teachers, for_all)  