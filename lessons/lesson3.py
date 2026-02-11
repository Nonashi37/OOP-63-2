                            # Encapsulation

# class BankAccount:
#
#     def __init__(self, login, balance, password):
#         self.login = login
#         self._balance = balance
#         self.__password = password
#
#
#     def m_login(self, login, password):
#         if self.login == login and self.__password == password:
#             return print("Ok")
#         else:
#             return print(" Wrong number or password ")
#
# andatr = BankAccount("andatr", 7890, 1235)
#
# andatr.m_login("andatr", "1235")







                            # Abstraction

# from abc import ABC, abstractmethod
#
#
# # Ето наш "Контракт"
# class Notification(ABC):
#     @abstractmethod
#     def send(self, message):
#         """Все, кто считает себя уведомлением, ОБЯЗАНЫ иметь етот метод"""
#
#
# # Реализация №1
# class EmailNotification(Notification):
#     def send(self, message):
#         print(f"Отправляем Email: {message} (через SMTP протокол)")
#
#
# # Реализация 2
# class SmsNotification(Notification):
#     def send(self, message):
#         print(f"Отправляем SMS: {message} (серез вышку связи)")
#
#
# # --- Использование ---
# def notify_user(service: Notification, text):
#     # Функции плевать, Кто ето. Она знает, что у него точно есть метод .send()
#     service.send(text)
#
#
# mail = EmailNotification()
# sms = SmsNotification()
#
# notify_user(mail, "Hello via email! ")
# notify_user(sms, "Hi via phone! ")



# Абстракция — это когда ты просишь жену «купить чего-нибудь к чаю».
#Ты задал абстрактную цель. А вот будет это Наполеон, печенье или суши
#это уже конкретная реализация, которая зависит от «бюджета» и «наличия в магазине».