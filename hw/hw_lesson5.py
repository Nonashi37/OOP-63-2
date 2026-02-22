# import functools
#
# def log_execution(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         # Печатаем имя и позиционные аргементы
#         print(f" Function {func.__name__} call argument {args}")
#
#         # Выполняем саму функцию
#         result = func(*args, **kwargs)
#
#         print(f"Result: {result}")
#         print("Function has finished")
#
#         return result
#     return wrapper
#
# @log_execution
# def add(a, b):
#     return a + b
#
# # test drive
# add(5, 3)


import functools

class User:
    def __init__(self, name, role):
        self.name = name
        self.role = role

def require_admin(func):
    @functools.wraps(func)
    def wrapper(user, *args, **kwargs):
        # Предполагаем, что user — это первый аргумент
        if user.role == "admin":
            return func(user, *args, **kwargs)
        else:
            print("Доступ запрещён")
            return None
    return wrapper

@require_admin
def delete_database(user):
    print(f"База данных удалена пользователем {user.name}")

# Проверка
admin = User("Alice", "admin")
guest = User("Bob", "user")

print("--- Попытка админа ---")
delete_database(admin)

print("\n--- Попытка юзера ---")
delete_database(guest)