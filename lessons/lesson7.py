import sqlite3

# Журнал
connect = sqlite3.connect("users.db")

cursor = connect.cursor()

cursor.execute('''
        CREATE TABLE IF NOT EXISTS users(
            name VARCHAR(50) NOT NULL,
            age INTEGER NOT NULL,
            hobby TEXT
        )
''')
connect.commit()

#CRUD create - read- update - delete

def create_user(name, age, hobby):
    cursor.execute(
        'INSERT INTO users(name, age, hobby) VALUES(?, ?, ?)',
        (name, age, hobby)
    )
    connect.commit()
    print(f"{name} created")

create_user("Amateru", 24, "read and listen different kings of books of any ganre")

def get_users():
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchmany(3)
    print(users)


def update_user(age, name):
    cursor.execute(
        'UPDATE users SET age = ? WHERE name = ?',
        (age, name)
    )
    connect.commit()
    print("Updated")
update_user(33, 2)
get_users()


def delete_user(rowid):
    cursor.execute(
        'DELETE FROM users WHERE rowid = ?',
        (rowid,)
    )
connect.commit()
print("deleted")


connect.close()