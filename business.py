#!/usr/bin/env python3
'''
Written by Josh Brown
This is a class object file with classes for a book application include
Book, Publisher, Author, Genre, Loan and CreateList. These objects interact
with lists in an application and help provide structure for the underlying
database
'''

from dataclasses import dataclass

@dataclass
class Book:
    bookID:int = 0
    title:str = ''
    author:str = ''
    publisher:str = ''
    year_published:int = 0
    genre:str = ''
    on_loan:str = ''

    def book_fromDB(self, row):
        self.bookID = row['bookID']
        self.title = row['Title']
        self.author = row['Author']
        self.publisher = row['Publisher']
        self.year_published = row['PublishedYear']
        self.genre = row['Genre']
        self.on_loan = row['OnLoan']
        
    def book_setList(self):
        return [self.bookID, self.title, self.author, self.publisher, self.year_published, self.genre, self.on_loan]

@dataclass
class Publisher:
    publisherID:int = 0
    name:str = ''

    def pub_setList(self):
        return [self.publisherID, self.name]

    def pub_fromDB(self, row):
        self.publisherID = row['publisherID']
        self.name = row['name']

@dataclass
class Author:
    authorID:int = 0
    name:str = ''

    def auth_setList(self):
        return [self.authorID, self.name]

    def auth_fromDB(self, row):
        self.authorID = row['authorID']
        self.name = row['name']

@dataclass
class Genre:
    genreID:int = 0
    genre:str = ''

    def gen_setList(self):
        return [self.genreID, self.genre]

    def gen_fromDB(self, row):
        self.genreID = row['genreID']
        self.genre = row['genre']

@dataclass
class Loan:
    loanID:int = 0
    value:str = ''

    def loan_setList(self):
        return [self.loanID, self.value]

    def loan_fromDB(self, row):
        self.loanID = row['loanID']
        self.value = row['Value']

class CreateList:
    def __init__(self):
        self.__lists = []
        self.hasBadData = False

    @property
    def count(self):
        return len(self.__lists)

    def get(self, index):
        if index >= self.count():
            return None
        else:
            return self.__lists[index]

    def add(self, data):
        self.__lists.append(data)

    def contact(self, user_list):
        for i in range(user_list.count):
            self.add(user_list.get(i))

    def __iter__(self):
        for data in self.__lists:
            yield data

    
def main():
    pass

if __name__ == '__main__':
    main()

    
