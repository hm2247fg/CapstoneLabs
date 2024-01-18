"""
INSTRUCTIONS:
1. Create a new class called Author.  Create a regular class, not a dataclass.
2. An Author has a name, and a list of books published.
3. When you create a new Author, they don't have any books. So create an empty books list
attribute in the __init__ method.
4. Your Author class should have a publish method, which takes the title of a book as an argument.
5. Add the title of this book to this object's books list.
6. Add a __str__ method that returns a String with the author's name, and the names of all of their
book's titles.
7. Write a main function to test your class, create some example authors, and publish some example books.
"""


class Author:

    def __init__(self, name):
        self.name = name
        self.books_list = []  # empty books list attribute

    def publish(self, title):  # publish method, which takes the title of a book as an argument
        self.books_list.append(title)  # Add the title of book to the object's books list

    def __str__(self):
        books_list = ', '.join(self.books_list)  # returns a String with the author's name, and their book's titles
        return f'Name: {self.name}. Books Published: {books_list}'


def main():

    shakespeare = Author('William Shakespeare')
    shakespeare.publish('Hamlet')
    shakespeare.publish('Richard III')
    print(shakespeare)

    hoover = Author('Colleen Hoover')
    hoover.publish('Verity')
    hoover.publish('It Starts with Us')
    print(hoover)


main()