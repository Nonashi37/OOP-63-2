class Hero:

    # Class constructor
    def __init__(self, nick, hp, lvl):
        # Атрибуты класса
        self.nick = nick
        self.hp = hp
        self.lvl = lvl


    # Методы класса
    def action(self):
        return f"The Base action of {self.nick} activated"

# Дочерний класс
class MageHero(Hero):
    def __init__(self, nick, hp, lvl, mp):
        super().__init__(nick, hp, lvl)
        self.mp = mp

    def action(self):
        return f" Ето новый метод дочернего класса {self.nick}"


asuna = Hero("Asuna", 564, 789)
kirito = Hero("Kirito", 889, 899)
mage_kirito = MageHero("Adventurer", 100, 1000, 99)

print(mage_kirito.action())
print(kirito.action())
print(asuna.action())



























# class A:
#     def speak(self):
#         print("A: Я начало всех начал.")
#
# class B(A):
#     def speak(self):
#         print("B: Я левая сторона ромба.")
#         super().speak()  # Передает эстафету дальше по списку MRO
#
# class C(A):
#     def speak(self):
#         print("C: Я правая сторона ромба.")
#         super().speak()  # Передает эстафету дедушке A
#
# class D(B, C):
#     def speak(self):
#         print("D: Я вершина (низ) ромба.")
#         super().speak()  # Начинает цепочку, вызывая B



