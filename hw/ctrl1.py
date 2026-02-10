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


class SmsService:
    def send_otp(self, phone):
        pass



class kg_sms(SmsService):
    def send_otp(self, phone):
        res = "<text>Код: 1234</text><phone>" + str(phone) + "</phone>"
        return res


class ru_sms(SmsService):
    def send_otp(self, phone):
        d = {}
        d["text"] = "Код: 1234"
        d["phone"] = phone
        return d


class MageHero:
    def __init__(self, n, l, h, m):
        self.name = n
        self.level = l
        self.hp = h
        self.mp = m

    def action(self):
        return "Маг " + self.name + " кастует заклинание! MP: " + str(self.mp)


class WarriorHero:
    def __init__(self, name, level, hp, st):
        self.name = name
        self.level = level
        self.hp = hp
        self.stamina = st

    def action(self):
        return "Воин %s рубит мечом! Уровень: %d" % (self.name, self.level)


class BankAccount:
    def __init__(self, hero, balance, pin, bank):
        self.hero = hero
        self.balance = balance
        self.pin = pin
        self.bank_name = bank

    def get_bank_name(self):
        return self.bank_name

    def bonus_for_level(self):
        return self.hero.level * 10

    def __str__(self):
        return self.hero.name + " | Баланс: " + str(self.balance) + " SOM"

    def __add__(self, other):
        if str(type(self.hero)) == str(type(other.hero)):
            return self.balance + other.balance
        else:
            return "Ошибка: Нельзя сложить счета героев разных классов!"

    def __eq__(self, other):
        if self.hero.name == other.hero.name and self.hero.level == other.hero.level:
            return True
        else:
            return False





mage1 = MageHero("Merlin", 80, 500, 150)
mage2 = MageHero("Merlin", 80, 500, 200)
warrior = WarriorHero("Conan", 50, 900, 20)
acc1 = BankAccount(mage1, 5000, "1234", "Simba")
acc2 = BankAccount(mage2, 3000, "0000", "Simba")
acc3 = BankAccount(warrior, 2500, "1111", "Simba")

print(mage1.action())
print(warrior.action())
print(acc1)
print(acc2)

print("Банк:", acc1.get_bank_name())
print("Бонус за уровень:", acc3.bonus_for_level(), "SOM")

print("\n=== Проверка __add__ ===")
print("Сумма счетов двух магов:", acc1 + acc2)
print("Сумма мага и воина:", acc1 + acc3)

print("\n=== Проверка __eq__ ===")
print("Mage1 == Mage2 ?", acc1 == acc2)
print("Mage1 == Warrior ?", acc1 == acc3)

sms = kg_sms()
print("\n", sms.send_otp("+996777123456"))

# huuh
