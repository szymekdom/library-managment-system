import json

class Book():
    def __init__(self, book_id, title, author, publishing_house):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.publishing_house =  publishing_house


    def show(self):
        print(f'{self.book_id}. {self.title} | {self.author} | {self.publishing_house}')

class Library():
    def __init__(self):
        self.books = {}
        self.book_id = 1

    def add_book(self, title, author, publishing_house):
        self.books[self.book_id] = Book(self.book_id, title, author, publishing_house)
        self.book_id+=1

    def del_book(self):
        del self.books[int(input('Enter the book id to delete: '))]

library = Library()

while True:

    print('\n1. Add a book\n2. Delete a book\n3. Modify a book\n4. Show books')
    
    choice = int(input('Choose an option: '))

   

    if choice==1:
            title = input("\nTitle: ")
            author = input("Author: ")
            publishing_house = input("Publishing house: ")
    
            library.add_book(title,author,publishing_house)

    if choice==2:
        print('\n')
        for id in library.books:
            print(f'{id}. {library.books[id].title}')

        library.del_book()

    if choice==3:
            print('\n')
            for i in library.books:
                print(f'{i}. {library.books[i].title} | {library.ooks[i].author} | {library.books[i].publishing_house}')
    
            mod_choice = int(input('Enter the book id to modify: '))
            print("Title: ")
            mod_input = input()
            if mod_input!="":
                library.books[mod_choice].title = mod_input
    
            print("Author: ")
            mod_input = input()
            if mod_input!="":
                library.books[mod_choice].author = mod_input
    
            print("Publishing house: ")
            mod_input = input()
            if mod_input!="":
                library.books[mod_choice].publishing_house = mod_input
    if choice==4:
        print('\n')
        for i in library.books:
            library.books[i].show()

