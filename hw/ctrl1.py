class Hero:

    # Class constructor
    def __init__(self, name, lvl, hp):
        # Атрибуты класса
        self.name = name
        self.lvl = lvl
        self.hp = hp

    def action(self):
        return f" {self.name} готов к бою! "

# Subclass Mage
class MageHero(Hero):
    def __init__(self, name, lvl, hp, mp):
        super().__init__(name, lvl, hp)
        self.mp = mp

    def action(self):
        return f" Маг {self.name} кастует заклинание! MP: {self.mp}"


# Subclass Warrior
class WarriorHero(MageHero):
    def action(self):
        return f" Воин {self.name} рубит мечом! Уровень: {self.lvl}"


#class BackAccount
class BankAccount:
    bank_name = "Simbank"
    def __init__(self, hero, balance, password):
      # Атрибуты класса
      self.hero = hero
      self._balance = balance
      self.__password = password

    def login(self, hero_to_check, password_to_check):
       if self.hero == hero_to_check and self.__password == password_to_check:
             return print("ok")
       else:
           return print("wrong")
    @property
    def full_info(self):
        return print(f" {self.hero.name}, Balance: {self._balance} ")

    @staticmethod
    def get_bank_name():
        return BankAccount.bank_name

    def bonus_per_level(self):
        return self.hero.lvl * 1.5

    # Маг методы
    def __add__(self, other):
        return self._balance + other._balance


    def __eq__(self, other):
        return self.hero.name == other.hero.name and self.hero.lvl == other.lvl


# Щбстрактный класс в разраюотке




#
#             def login(self, login, password):
#                 if self.login == login and self.__password == password:
#                     return print("Ok")
#                 else:
#                     return print("Nope")
#
#         andatr = BankAccount("andatr", 1000, 1235)
#
#         print("Hello world")