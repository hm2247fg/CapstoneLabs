"""
INSTRUCTIONS:
1. Start with the program from part 1.
2. In this version, an author can't publish two books with the same name.
3. When the publish method is called, print an error message if the book given
has the same name as a book currently in the books list. Do not add the duplicate book.
(In other words, make sure the Author object's book list doesn't already contain that name).
"""


class Author:

    def __init__(self, name):
        self.name = name
        self.books_list = []

    def publish(self, title):
        if title in self.books_list:  # Author can't publish two books with the same name
            print('This book has already been published.')
        else:
            self.books_list.append(title)

    def __str__(self):
        books_list = ', '.join(self.books_list)
        return f'Name: {self.name}. Books Published: {books_list}'


def main():

    shakespeare = Author('William Shakespeare')
    shakespeare.publish('Hamlet')
    shakespeare.publish('Hamlet')
    shakespeare.publish('Richard III')
    print(shakespeare)

    hoover = Author('It Ends with Us')
    hoover.publish('Verity')
    hoover.publish('It Starts with Us')
    print(hoover)


main()

