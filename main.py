import json

class Book():
    def __init__(self, title, author, publishing_house):
        self.title = title
        self.author = author
        self.publishing_house =  publishing_house

books = {}
book_id = 1

while True:

    print('1. Add a book\n2. Delete a book\n3. Modify a book')
    
    choice = int(input('Choose an option: '))

    if choice==1:
            title = input("Title: ")
            author = input("Author: ")
            publishing_house = input("Publishing house: ")
    
            books[book_id] = Book(title, author, publishing_house)
            book_id += 1

    if choice==2:
        for id in books:
            print(f'{id}. {books[id].title}')

        del books[int(input('Enter the book id to delete: '))]

    if choice==3:
            for i in books:
                print(f'{i}. {books[i].title} | {books[i].author} | {books[i].publishing_house}')
    
            mod_choice = int(input('Enter the book id to modify: '))
            print("Title: ")
            mod_input = input()
            if mod_input!="":
                books[mod_choice].title = mod_input
    
            print("Author: ")
            mod_input = input()
            if mod_input!="":
                books[mod_choice].author = mod_input
    
            print("Publishing house: ")
            mod_input = input()
            if mod_input!="":
                books[mod_choice].publishing_house = mod_input

