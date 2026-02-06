# class Hero:
#
#     # Class constructor
#     def __init__(self, nick, hp, lvl):
#         # Атрибуты класса
#         self.nick = nick
#         self.hp = hp
#         self.lvl = lvl
#
#
#     # Методы класса
#     def action(self):
#         return f"{self.nick} base action activate1"
#
#
# # Обьект/екземпляр класса
# kirito = Hero("Kiriro", 1000, 100)
# asuna = Hero("Asuna", 1100, 101)
#
#
# print(kirito.action())
# print(asuna.action())



# HomeWork

class Character:
    def __init__(self, name, type, speed):
        self.name = name
        self.type = type
        self.speed = speed

    def show(self):
        return f" Name: {self.name}, tepe: {self.type}, speed {self.speed}"

    def action(self):
      if self.type == "Warrior":
        extra_speed = 10
        return f" If Necessary:  the {self.name}'s speed from {self.speed} to {self.speed + extra_speed}"
      elif self.type == "Archer":
        extra_speed = 15
      return f" If Necessary: the {self.name}'s speed from {self.speed} to {self.speed + extra_speed}"



Warior = Character("Alduin", "Warrior", 20)
Archer = Character("Legolas", "Archer", 45)

print(Warior.show())
print(Warior.action())

print(Archer.show())
print(Archer.action())
