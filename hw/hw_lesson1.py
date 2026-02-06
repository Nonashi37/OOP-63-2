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
