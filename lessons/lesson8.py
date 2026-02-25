import sqlite3
import os

connect = sqlite3.connect("grades.db")
cursor = connect.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(50) NOT NULL
)
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS grades(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        subject VARCHAR(40),
        grade INTEGER NOT NULL,
        user_id INTEGER NOT NULL,
        FOREIGN KEY (user_id) REFERENCES users(id)
    )
""")

connect.commit()


def create_users(name):
    cursor.execute("INSERT INTO users (name) VALUES (?)", (name,))
    connect.commit()
    print("User added")
    return cursor.lastrowid

def create_grade(subject, grade, user_id):
    cursor.execute(
        "INSERT INTO grades (subject, grade, user_id) VALUES (?, ?, ?)",
        (subject, grade, user_id),
    )
    connect.commit()
    print("Grade added")
    return cursor.lastrowid


def get_user_and_grade():
    cursor.execute(
        """
        SELECT users.name, grades.subject, grades.grade
        FROM users INNER JOIN grades ON users.id = grades.user_id
        """
    )

    users = cursor.fetchall()

    for i in users:
        print(f"{i[0]} -- {i[1]} -- {i[2]}")


def show_users():
    cursor.execute("SELECT id, name FROM users")
    rows = cursor.fetchall()
    for row in rows:
        print(row)


def show_grades():
    cursor.execute("SELECT id, subject, grade, user_id FROM grades")
    rows = cursor.fetchall()
    for row in rows:
        print(row)


def create_view():
    cursor.execute('''
        CREATE VIEW IF NOT EXISTS  my_view AS
        SELECT name, subject, grade
        FROM users LEFT JOIN grades ON users.id = grades.user_id
        WHERE grade > 4
    ''')
    connect.commit()

create_view
print("View created")



if __name__ == "__main__":
    try:
        print("DB file:", os.path.abspath("grades.db"))
        choice = input("1) Add user+grade\n2) Show users\n3) Show grades\n4) Show report (join)\nChoose: ")

        if choice == "1":
            name = input("User name: ")
            subject = input("Subject: ")
            grade = int(input("Grade (number): "))

            user_id = create_users(name)
            create_grade(subject, grade, user_id)
            get_user_and_grade()
        elif choice == "2":
            show_users()
        elif choice == "3":
            show_grades()
        elif choice == "4":
            get_user_and_grade()
        else:
            print("Unknown choice")
    finally:
        connect.close()

