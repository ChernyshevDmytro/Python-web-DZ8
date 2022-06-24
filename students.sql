-- 3 groups
DROP TABLE IF EXISTS list_of_groups;
CREATE TABLE list_of_groups (
    id INTEGER PRIMARY KEY AUTOINCREMENT,    
    group_number INT NOT NULL   
);

-- 5 subjects
DROP TABLE IF EXISTS list_of_subjects;
CREATE TABLE list_of_subjects (
    id INTEGER PRIMARY KEY AUTOINCREMENT,    
    subject_name VARCHAR(255) UNIQUE NOT NULL  
);

-- 3 teachers
DROP TABLE IF EXISTS list_of_teachers;
CREATE TABLE list_of_teachers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,    
    teacher_name VARCHAR(255) UNIQUE NOT NULL  
);

-- 10 grades
DROP TABLE IF EXISTS list_of_grades;
CREATE TABLE list_of_grades (
    id INTEGER PRIMARY KEY AUTOINCREMENT,    
    grade INT NOT NULL   
);

DROP TABLE IF EXISTS list_of_students;
CREATE TABLE list_of_students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_name VARCHAR(50) NOT NULL,
    group_number INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (group_number) REFERENCES list_of_groups (group_number)
      ON DELETE CASCADE
      ON UPDATE CASCADE
);

DROP TABLE IF EXISTS total;
CREATE TABLE total (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER,

    student_name VARCHAR(50),

    teacher_name VARCHAR(50),
    subject_name VARCHAR(50) NOT NULL,
    grade INT NOT NULL,
    

    graded_at DATE NOT NULL,

    FOREIGN KEY (student_id) REFERENCES list_of_students (id)
      ON DELETE CASCADE
      ON UPDATE CASCADE

    FOREIGN KEY (student_name) REFERENCES list_of_students (student_name)
      ON DELETE CASCADE
      ON UPDATE CASCADE    

    FOREIGN KEY (subject_name) REFERENCES list_of_subjects (subject_name)
      ON DELETE CASCADE
      ON UPDATE CASCADE 

    FOREIGN KEY (teacher_name) REFERENCES list_of_teachers (teacher_name)
      ON DELETE CASCADE
      ON UPDATE CASCADE

    FOREIGN KEY (grade) REFERENCES list_of_grades (grade)
      ON DELETE CASCADE
      ON UPDATE CASCADE      

);