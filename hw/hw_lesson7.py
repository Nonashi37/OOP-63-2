import sqlite3

# Журнал (Connection management)
# Совет: используй context manager 'with', чтобы не забыть закрыть коннект
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

# --- CRUD Operations ---

def create_user(name, age, hobby):
    cursor.execute(
        'INSERT INTO users(name, age, hobby) VALUES(?, ?, ?)',
        (name, age, hobby)
    )
    connect.commit()
    print(f"User {name} created")

def get_users():
    cursor.execute('SELECT rowid, * FROM users') # Добавил rowid для наглядности
    users = cursor.fetchall()
    print(f"Current users: {users}")

def update_user(age, name):
    cursor.execute(
        'UPDATE users SET age = ? WHERE name = ?',
        (age, name)
    )
    connect.commit()
    print(f" User {name} updated to age {age}")

def delete_user(user_id):
    cursor.execute(
        'DELETE FROM users WHERE rowid = ?',
        (user_id,)
    )
    connect.commit() # Теперь внутри функции!
    print(f"🗑 User with ID {user_id} deleted")

# --- Almighty Mass Operations ---

def update_users(ids, name=None, age=None, hobby=None):
    ids = list(ids)
    if not ids:
        print("No IDs provided")
        return

    updates = []
    params = []

    if name is not None:
        updates.append("name = ?")
        params.append(name)
    if age is not None:
        updates.append("age = ?")
        params.append(age)
    if hobby is not None:
        updates.append("hobby = ?")
        params.append(hobby)

    if not updates:
        print("Nothing to update, bro")
        return

    # FIX: Исправленный генератор плейсхолдеров
    placeholders = ", ".join("?" for _ in ids)
    query = f"UPDATE users SET {', '.join(updates)} WHERE rowid IN ({placeholders})"

    # Объединяем параметры для SET и для WHERE IN
    cursor.execute(query, params + ids)
    connect.commit()
    print(f" Bulk update for IDs {ids} finished.")

def delete_users(ids):
    ids = list(ids)
    if not ids:
        print("No IDs provided")
        return

    placeholders = ", ".join("?" for _ in ids)
    query = f"DELETE FROM users WHERE rowid IN ({placeholders})"

    cursor.execute(query, ids)
    connect.commit()
    print(f" Nuked users with IDs {ids}")

# --- ТЕСТЫ ---
create_user("Amateru", 24, "Gaming and Python")
get_users()

# Массовый апдейт
update_users([1, 2], age=18, hobby="Coding like a pro")

# Массовое удаление
delete_users([3, 4])


def check_results():
    print("\n--- FINAL CHECK ---")
    # Явно запрашиваем rowid, чтобы понять, кто есть кто
    cursor.execute('SELECT rowid, name, age, hobby FROM users')
    rows = cursor.fetchall()

    if not rows:
        print("Database is empty. Either everyone was deleted or no one was created.")
    else:
        for row in rows:
            print(f"ID: {row[0]} | Name: {row[1]} | Age: {row[2]} | Hobby: {row[3]}")
    print("----------------------\n")


# Сначала создадим парочку юзеров для теста
create_user("User_1", 20, "Testing")
create_user("User_2", 30, "Bug hunting")

# Проверяем список ДО
print("Before mass operations:")
check_results()

# Тестим Almighty Update для ID 1 и 2
update_users([1, 2], age=99, hobby="Retired Developer")

# Проверяем результат
print("After Update:")
check_results()

# Тестим Delete для ID 1
delete_users([1])

print("After Delete:")
check_results()

connect.close()