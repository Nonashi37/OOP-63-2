class Movie:
    def __init__(self, title, duration):
        self.title = title
        self.duration = duration

    def __str__(self):
        return f" {self.title} {self.duration} minutes"

    def __add__(self, other):
        if type(other) == Movie:
            return f"{self.duration + other.duration} минут жизни потеряешь на диване"
        else:
            return f"NotImplemented"

    def __eq__(self, other):
        if not isinstance(other, Movie):
            return print("False")

        return self.title == other.title and self.duration == other.duration



class Library:
    def __init__(self, movies):
        self.movies = movies

    def __getitem__(self, index):
        # Делаем так что бы к обьекту можно было обрашатся по индексу
        return self.movies[index]

    def __len__(self):
        # Сколько Фильмов в каталоге
        return len(self.movies)

    def __str__(self):
        # Красивый список с номерами
        result = ""
        for i, movie in enumerate(self.movies):
            result += f"{i + 1}. {movie}\n"
        return result.strip()


class User:
    def __init__(self, name, library):
        self.name = name
        self.library = library

    def __call__(self, *args, **kwargs):
        # Когда мы вызываем обьект как функцию user(
        print(f"User {self.name} is watching movies")

    def __str__(self):
        return f"User: {self.name} | MOvies: {len(self.library)}"



# Создаем Фильмы:
m1 = Movie("Matrix", 136)
m2 = Movie("Inception", 148)
m3 = Movie("Inception", 169)
m4 = Movie("Inception", 148)
m5 = Movie("Jumanji", 148)
m6 = Movie("Avatar", 162)
m7 = Movie("OnceUponATimeInHOLLYWOOD", 201)

# Собираем Библеотеку
library = Library([m1, m2,  m3])

# Создаем Юзера
user = User("Alex", library)

# Понеслась Проверка
print(m1)
print(m1 + m2)
print(m1 == m2)
print(library[1])
print(len(library))
print(library)
print(user)
user()



# print(f"movie1 == movie2: {m1 == m2}")
# print(f"movie1 == movie3: {m1 == m3}")
# print(f"movie 1 + movie4: {m1 + m4}")

