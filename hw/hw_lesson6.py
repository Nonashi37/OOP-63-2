# class Book:
#
#     def __init__(self, title, author, num_pages):
#         self.title = title
#         self.author = author
#         self.num_pages = num_pages
#
#     def __str__(self):
#         return f"{self.title} by {self.author}, {self.num_pages} pages"
#
#     def __eq__(self, other):
#         return self.title == other.title and self.author == other.author
#
#     def __gt__(self, other):
#         return self.num_pages < other.num_pages
#
#     def __gt__(self, other):
#         return self.num_pages > other.num_pages
#
#     def __add__(self, other):
#         return f"{self.num_pages + other.num_pages} pages"
#
#     def __contains__(self, keyword):
#         return keyword in self.title or keyword in self.author
#
#     def __getitem__(self, item):
#         if item == "title":
#             return self.title
#         elif item == "author":
#             return self.author
#         elif item == "num_pages":
#             return self.num_pages
#         else:
#             return f"item '{item}' was not found bro"
#
#
# book1 = Book("The Hobbit", "J,R,R. Talkien", 319)
# book2 = Book("Harry Potter and the half blood Prince", "J.K. Rowling", 289)
# book3 = Book("Alice in 'Lion' Wonderland", "Mark Stilinsky", 273)
#
#
# print(book3)
# print(book2 == book1)
# print(book2 + book3)
# print("Rowling" in book2)
# print(book1['author'])
# print(book3['audio'])
# print("hello")


nums = [2, 7, 11, 15]
target = int(input("Write: "))
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == target:
            print(nums[i])
            print(nums[j])
            print(f"indexes: [{i}], [{j}]")
            break
