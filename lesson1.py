class Hero:

    # Class constructor
    def __init__(self, nick, hp, lvl):
        # Атрибуты класса
        self.nick = nick
        self.hp = hp
        self.lvl = lvl


    # Методы класса
    def action(self):
        return f"{self.nick} base action activate1"


# Обьект/екземпляр класса
kirito = Hero("Kiriro", 1000, 100)
asuna = Hero("Asuna", 1100, 101)

print(kirito.action())
print(asuna.action())