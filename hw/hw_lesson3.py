class UserAccaunt:
    def __init__(self, username, balance, pin):
        self.username = username
        self._balance = balance
        self.__pin = pin

    # \getter для зашашенного атрибута balance
    @property
    def balance(self):
        return f" На счету у {self.username}: {self._balance} SOM "

    # Метод для проверки доступа к PIN
    def check_pin(self, input_pin):
        # Проверяет совпадает ли введенный PIN с введенным
        return self.__pin == input_pin # IF input PIN == self.__pin return

    # Метод для изменения приватного атрибута
    def reset_pin(self, old_pin, new_pin):
        """"Сменить Пин код при условии если известен старый"""
        if self.check_pin(old_pin):
            self.__pin = new_pin
            print(" Success PIN Успешно изменен ")
        else:
            print(" Error 303 old PIN is incorrect ")

# Демонстрация что работает

user = UserAccaunt("Dmitry_Koshyenko", 1585999, "5467")

print(f"User: {user.username}")
print(user.balance)

# Пробуем достучатся приватного доступа на прямую
print("\n--- Попытка взлома ---")
try:
    print(user.__pin)
except AttributeError:
    print(" Error: Python не дает обратится к __pin напрямую Инкапсуляция в деле")


# работаем через Официал методы
print("\n--- Проверка Доступа ---")
is_valid = user.check_pin("1234")
print(f"Введен PIN 1234. Верно? {is_valid}")

is_valid = user.check_pin("5467")
print(f"Введен PIN 5467. Верно? {is_valid}")

# Смена пароля
print("\n--- Changing the PIN ---")
user.reset_pin("000", "1111") # won't work
user.reset_pin("5467", "7788") # will work




                        # Part 2 Encapsulation
# from abc import ABC, abstractmethod
# import json
#
#
# # 1. Наш Абстрактный Класс - "Контракт"
# class NotificationService(ABC):
#
#     @abstractmethod
#     def send_to_phone(self, phone, message):
#         """Этот метод должен отправить SMS"""
#         pass
#
#     @abstractmethod
#     def send_to_email(self, email, message):
#         """Этот метод должен отправить Email"""
#         pass
#
#
# # 2. Наследник №1: Сервис для Кыргызстана (KGSms)
# # Тут мы добавляем специфику региона
# class KyrgyzstanService(NotificationService):
#     def send_to_phone(self, phone, message):
#         # Допустим, мы всегда приводим номер к формату +996
#         clean_phone = phone.replace(" ", "").replace("-", "")
#         if not clean_phone.startswith("+996"):
#             clean_phone = f"+996{clean_phone[-9:]}"
#
#         return f"[KG-SMS] Отправлено на {clean_phone}: {message}"
#
#     def send_to_email(self, email, message):
#         return f"[KG-MAIL] Письмо для {email} улетело через сервер Bishkek-Main."
#
#
# # 3. Наследник №2: Сервис в формате JSON (для API или логов)
# # Тут мы возвращаем данные в виде словаря/JSON
# class JsonApiService(NotificationService):
#     def send_to_phone(self, phone, message):
#         payload = {
#             "type": "SMS",
#             "recipient": phone,
#             "content": message,
#             "status": "queued"
#         }
#         return json.dumps(payload, ensure_ascii=False)
#
#     def send_to_email(self, email, message):
#         payload = {
#             "type": "EMAIL",
#             "address": email,
#             "body": message,
#             "priority": "high"
#         }
#         return json.dumps(payload, ensure_ascii=False)
#
# # --- Демонстрация ---
#
# def run_test():
#     print("🚀 Запуск системы уведомлений...\n")
#
#     # Создаем сервисы
#     kg_provider = KyrgyzstanService()
#     api_provider = JsonApiService()
#
#     # Тестируем KG сервис
#     print("--- Работаем с KyrgyzstanService ---")
#     print(kg_provider.send_to_phone("0777 12-34-56", "Ваш код: 999"))
#     print(kg_provider.send_to_email("dev@pro.kg", "Завтра деплой в 5 утра!"))
#
#     # Тестируем API сервис
#     print("\n--- Работаем с JsonApiService ---")
#     print(api_provider.send_to_phone("+79001112233", "Hello from API!"))
#     print(api_provider.send_to_email("boss@google.com", "We need a raise."))
#
#     # Проверка "защиты" абстракции
#     print("\n--- Проверка защиты ---")
#     try:
#         base = NotificationService() # Попытка создать "просто сервис"
#     except TypeError as e:
#         print(f"⛔️ Ошибка: {e}")
#         print("Система: Нельзя создать экземпляр абстрактного класса! Контракт работает.")
#
# run_test()





