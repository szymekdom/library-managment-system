import json

class Book():
    def __init__(self, title, author, publishing_house):
        self.title = title
        self.author = author
        self.publishing_house =  publishing_house

books = {}

while True:

    print('1. Add a book\n2. Delete a book\n3. Modify a book')
    
    choice = int(input('Choose an option: '))

    if choice==1:
            title = input("Title: ")
            author = input("Author: ")
            publishing_house = input("Publishing house: ")
    
            books[title] = Book(title, author, publishing_house)

    if choice==2:
        for title in books:
            print(books[title].title)

        del books[input('Enter the title to delete: ')]

    

