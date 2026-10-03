import json

class Book():
    def __init__(self, book_id, title, author, publishing_house):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.publishing_house =  publishing_house


    def show(self):
        print(f'{self.book_id}. {self.title} | {self.author} | {self.publishing_house}')


class User():
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.borrowed_books = []

    def show(self):
        print(f'{self.user_id}. {self.name}')



class Library():
    def __init__(self):
        self.books = {}
        self.book_id = 1
        self.users = {}
        self.user_id = 1

    def add_book(self, title, author, publishing_house):
        self.books[self.book_id] = Book(self.book_id, title, author, publishing_house)
        self.book_id+=1

    def del_book(self):
        del self.books[int(input('Enter the book id to delete: '))]

    def search_book(self, title):
        c = 0
        for book in self.books.values():
            if title.lower() in book.title.lower():
                book.show()
                c+=1
        if c == 0:
            print("Book not found")

    def add_user(self, name):
        self.users[self.user_id] = User(self.user_id, name)
        self.user_id += 1

    def delete_user(self):
        del self.users[int(input('Enter the user id to delete: '))]
    

library = Library()

while True:

    print('\n1. Add a book\n2. Delete a book\n3. Modify a book\n4. Show books\n5. Search books\n6. Add user\n7. Delete user')
    
    choice = int(input('Choose an option: '))

   

    if choice==1:
            title = input("\nTitle: ")
            author = input("Author: ")
            publishing_house = input("Publishing house: ")
    
            library.add_book(title,author,publishing_house)

    if choice==2:
        print('\n')
        for book_id in library.books:
            print(f'{book_id}. {library.books[book_id].title}')

        library.del_book()

    if choice==3:
            print('\n')
            for i in library.books:
                print(f'{i}. {library.books[i].title} | {library.books[i].author} | {library.books[i].publishing_house}')
    
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

    if choice == 5:
        print('\n')
        title = input("Enter title to search: ")
        library.search_book(title)
        input()
    if choice == 6:
        print('\n')
        name = input("Enter the user: ")
        library.add_user(name)
        
    if choice == 7:
        print('\n')
        for user_id in library.users:
                print(f'{user_id}. {library.users[user_id].name}')
        library.delete_user()