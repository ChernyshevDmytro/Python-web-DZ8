-- 3 groups
DROP TABLE IF EXISTS groups;
CREATE TABLE groups (
    id INTEGER PRIMARY KEY AUTOINCREMENT,    
    number INT NOT NULL   
);

-- 5 subjects
DROP TABLE IF EXISTS subjects;
CREATE TABLE subjects (
    id INTEGER PRIMARY KEY AUTOINCREMENT,    
    subject VARCHAR(255) UNIQUE NOT NULL  
);

-- 3 teachers
DROP TABLE IF EXISTS teachers;
CREATE TABLE teachers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,    
    full_name VARCHAR(255) UNIQUE NOT NULL  
);

DROP TABLE IF EXISTS students;
CREATE TABLE students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    full_name VARCHAR(50) NOT NULL,    
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

);

DROP TABLE IF EXISTS total;
CREATE TABLE total (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER,    
    student_group INT,
    teacher_id INTEGER,
    subject_id INTEGER NOT NULL,
    grade INT NOT NULL,    
    graded_at DATE NOT NULL,

    FOREIGN KEY (student_id) REFERENCES students (id)
      ON DELETE CASCADE
      ON UPDATE CASCADE

    FOREIGN KEY (teacher_id) REFERENCES teachers (id)
      ON DELETE CASCADE
      ON UPDATE CASCADE    

    FOREIGN KEY (subject_id) REFERENCES subjects (id)
      ON DELETE CASCADE
      ON UPDATE CASCADE    
    
    FOREIGN KEY (student_group) REFERENCES groups (number)
      ON DELETE CASCADE
      ON UPDATE CASCADE


);