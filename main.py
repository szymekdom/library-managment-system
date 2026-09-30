import json

class Book():
    def __init__(self, title, author, publishing_house):
        self.title = title
        self.author = author
        self.publishing_house =  publishing_house

books = {}

while True:
    print('1. Add a book\n')
    print('Choose an option: ')
    choice = int(input())

    if choice==1:
            title = input("Title: ")
            author = input("Author: ")
            publishing_house = input("Publishing house: ")
    
            books[title] = Book(title, author, publishing_house)
            
