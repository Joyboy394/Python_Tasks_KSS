class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display(self):
        print(f"Title: {self.title}, Author: {self.author}, Price: {self.price}")


class EBook(Book):
    def __init__(self, title, author, price, file_size):
        super().__init__(title, author, price)
        self.file_size = file_size

    def display(self):
        super().display()
        print(f"File Size: {self.file_size} MB")


book1 = Book("The Alchemist", "Paulo Coelho", 350)
ebook1 = EBook("Atomic Habits", "James Clear", 250, 15)

print("Physical Book Details:")
book1.display()

print("\nEBook Details:")
ebook1.display()
