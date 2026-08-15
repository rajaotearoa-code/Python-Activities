import sqlite3

DATABASE_NAME = "academic_system.db"


def create_connection():
    """Establishes connection to the SQLite database file."""
    return sqlite3.connect(DATABASE_NAME)


def initialize_database():
    """Creates tables based on the ER model with primary and foreign keys."""
    conn = create_connection()
    cursor = conn.cursor()

    # Enable foreign key constraint support in SQLite
    cursor.execute("PRAGMA foreign_keys = ON;")

    # 1. Students Table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            student_id TEXT PRIMARY KEY,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            birth_date TEXT
        );
    """)

    # 2. Lecturers Table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS lecturers (
            lecturer_id TEXT PRIMARY KEY,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            address TEXT
        );
    """)

    # 3. Courses / Subjects Table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS courses (
            course_code TEXT PRIMARY KEY,
            course_name TEXT NOT NULL,
            credits INTEGER NOT NULL
        );
    """)

    # 4. Enrollments Table (Linking Students and Courses)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS enrollments (
            enrollment_id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id TEXT NOT NULL,
            course_code TEXT NOT NULL,
            enrollment_date TEXT NOT NULL,
            FOREIGN KEY (student_id) REFERENCES students(student_id),
            FOREIGN KEY (course_code) REFERENCES courses(course_code)
        );
    """)

    conn.commit()
    conn.close()


def populate_sample_data():
    """Inserts 3 courses, 2 lecturers, 5 students, and sample enrollments."""
    conn = create_connection()
    cursor = conn.cursor()

    # Clear existing data to avoid duplicate key errors on rerun
    cursor.execute("DELETE FROM enrollments;")
    cursor.execute("DELETE FROM courses;")
    cursor.execute("DELETE FROM lecturers;")
    cursor.execute("DELETE FROM students;")

    # Insert 3 Courses
    courses_data = [
        ("CS101", "Introduction to Software Engineering", 15),
        ("CS102", "Database Design & SQL", 15),
        ("CS103", "Data Structures & Algorithms", 15)
    ]
    cursor.executemany("INSERT INTO courses VALUES (?, ?, ?);", courses_data)

    # Insert 2 Lecturers
    lecturers_data = [
        ("L001", "Alan", "Turing", "alan.turing@university.ac.nz", "10 Science Rd"),
        ("L002", "Ada", "Lovelace", "ada.lovelace@university.ac.nz", "22 Computing Way")
    ]
    cursor.executemany("INSERT INTO lecturers VALUES (?, ?, ?, ?, ?);", lecturers_data)

    # Insert 5 Students
    students_data = [
        ("S1001", "Rajneesh", "Kumar", "1998-05-12"),
        ("S1002", "Emily", "Watson", "2001-08-22"),
        ("S1003", "Michael", "Chen", "2000-02-14"),
        ("S1004", "Sophia", "Patel", "1999-11-30"),
        ("S1005", "Liam", "Smith", "2002-04-18")
    ]
    cursor.executemany("INSERT INTO students VALUES (?, ?, ?, ?);", students_data)

    # Insert Student Enrolments
    # Notice: S1001 and S1002 are enrolled in MULTIPLE courses
    enrollments_data = [
        ("S1001", "CS101", "2026-02-20"),
        ("S1001", "CS102", "2026-02-21"),
        ("S1001", "CS103", "2026-02-22"),
        ("S1002", "CS101", "2026-02-20"),
        ("S1002", "CS102", "2026-02-23"),
        ("S1003", "CS101", "2026-02-20"),
        ("S1004", "CS102", "2026-02-24"),
        ("S1005", "CS103", "2026-02-25")
    ]
    cursor.executemany("INSERT INTO enrollments (student_id, course_code, enrollment_date) VALUES (?, ?, ?);", enrollments_data)

    conn.commit()
    conn.close()
    print("[+] Database populated with sample records successfully.")


def query_students_per_course():
    """Query 1: How many students are registered in each course?"""
    conn = create_connection()
    cursor = conn.cursor()

    sql_query = """
        SELECT 
            courses.course_code,
            courses.course_name,
            COUNT(enrollments.student_id) AS total_enrolled
        FROM courses
        LEFT JOIN enrollments ON courses.course_code = enrollments.course_code
        GROUP BY courses.course_code, courses.course_name;
    """

    cursor.execute(sql_query)
    results = cursor.fetchall()
    conn.close()

    print("\n" + "=" * 65)
    print("QUERY 1: NUMBER OF STUDENTS REGISTERED IN EACH COURSE")
    print("=" * 65)
    for code, name, count in results:
        print(f"[{code}] {name:<38} -> {count} student(s)")


def query_multi_enrolled_students():
    """Query 2: Names and IDs of students enrolled in more than one course."""
    conn = create_connection()
    cursor = conn.cursor()

    sql_query = """
        SELECT 
            students.student_id,
            students.first_name || ' ' || students.last_name AS full_name,
            COUNT(enrollments.course_code) AS course_count
        FROM students
        JOIN enrollments ON students.student_id = enrollments.student_id
        GROUP BY students.student_id, full_name
        HAVING COUNT(enrollments.course_code) > 1;
    """

    cursor.execute(sql_query)
    results = cursor.fetchall()
    conn.close()

    print("\n" + "=" * 65)
    print("QUERY 2: STUDENTS ENROLLED IN MORE THAN ONE COURSE")
    print("=" * 65)
    for s_id, name, count in results:
        print(f"ID: {s_id:<8} | Name: {name:<22} | Enrolled in: {count} courses")
    print("=" * 65)


def main():
    initialize_database()
    populate_sample_data()
    query_students_per_course()
    query_multi_enrolled_students()


if __name__ == "__main__":
    main()