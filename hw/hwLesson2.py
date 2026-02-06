class Worker:
    def __init__(self, name):
        # Атрибут
        self.name = name

    # Метод
    def work(self):
        print(f' The Worker "{self.name}" works ')


# SubClasses
class Developer(Worker):
    def work(self):
        print(f' The Developer "{self.name}" writes code')


class Designer(Worker):
    def work(self):
        print(f' The Designer "{self.name}" creates design')


#Polemorphism

workers = [
    Worker("Sam Winchester"),
    Developer("Alice Argent"),
    Designer("Katy Perry")
]


def finalize(Worker):
    Worker.work()

for w in workers:
    finalize(w)

