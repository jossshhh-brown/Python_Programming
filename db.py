#!/usr/bin/env python3
'''
Written by Josh Brown
This is a databse file to connect to and work with the data in a
schema named "Final", formatted in SQLite formatting
'''

import sqlite3
from contextlib import closing
from business import Book, CreateList, Publisher, Author, Genre, Loan

conn = None

# Connect to the database
def connect_db():
    global conn
    if not conn:
        FILE = 'Final.sqlite'
        conn = sqlite3.connect(FILE)
        conn.row_factory = sqlite3.Row

# Locate Author data from the database
def get_author():
    try:
        query = '''
                SELECT authorID, name
                FROM Authors
                '''
        with closing(conn.cursor()) as c:
            c.execute(query)
            rows = c.fetchall()

            authors = CreateList()
            for row in rows:
                data = Author()
                data.auth_fromDB(row)
                authors.add(data)
            return authors
        
    except sqlite3.OperationalError:
        return None

# Locate Genre data from the database
def get_genre():
    try:
        query = '''
                SELECT genreID, genre
                FROM Genres
                '''
        with closing(conn.cursor()) as c:
            c.execute(query)
            rows = c.fetchall()

            genres = CreateList()
            for row in rows:
                data = Genre()
                data.gen_fromDB(row)
                genres.add(data)
            return genres
        
    except sqlite3.OperationalError:
        return None

# Locate On Loan data from the database
def get_loan():
    try:
        query = '''
                SELECT loanID, Value
                FROM Loaned
                '''
        with closing(conn.cursor()) as c:
            c.execute(query)
            rows = c.fetchall()

            loans = CreateList()
            for row in rows:
                data = Loan()
                data.loan_fromDB(row)
                loans.add(data)
            return loans
        
    except sqlite3.OperationalError:
        return None

# Locate Publisher data from the database
def get_publisher():
    try:
        query = '''
                SELECT publisherID, name
                FROM Publishers
                '''
        with closing(conn.cursor()) as c:
            c.execute(query)
            rows = c.fetchall()

            publishers = CreateList()
            for row in rows:
                data = Publisher()
                data.pub_fromDB(row)
                publishers.add(data)
            return publishers
        
    except sqlite3.OperationalError:
        return None


# Locate all book data from the database
def get_all_books():
    try:
        query = '''
                SELECT b.bookID,
                       b.title AS Title,
                       a.name AS Author,
                       g.genre AS Genre,
                       p.name AS Publisher,
                       b.yearPublished AS PublishedYear,
                       l.Value AS OnLoan
                FROM Books AS b
                  INNER JOIN Authors AS a USING(authorID)
                  INNER JOIN Genres AS g ON b.genreID = g.genreID
                  INNER JOIN Publishers AS p ON b.publisherID = p.publisherID
                  INNER JOIN Loaned AS l ON b.loanID = l.loanID
                ORDER BY b.bookID ASC
                '''
        with closing(conn.cursor()) as c:
            c.execute(query)
            rows = c.fetchall()

            books = CreateList()
            for row in rows:
                data = Book()
                data.book_fromDB(row)
                books.add(data)
            return books
        
    except sqlite3.OperationalError:
        return None

# Locate books that are On Loan = true from the database
def get_loaned_books():
    try:
        query = '''
                SELECT b.bookID,
                       b.title,
                       a.name AS author,
                       g.genre AS Genre,
                       p.name AS Publisher,
                       b.yearPublished AS PublishedYear,
                       l.Value AS OnLoan
                FROM Books AS b
                  INNER JOIN Authors AS a USING(authorID)
                  INNER JOIN Genres AS g ON b.genreID = g.genreID
                  INNER JOIN Publishers AS p ON b.publisherID = p.publisherID
                  INNER JOIN Loaned AS l ON b.loanID = l.loanID
                WHERE OnLoan = 'True'
                ORDER BY b.title ASC
                '''
        with closing(conn.cursor()) as c:
            c.execute(query)
            rows = c.fetchall()

            loans = CreateList()
            for row in rows:
                data = Book()
                data.book_fromDB(row)
                loans.add(data)
            return loans
        
    except sqlite3.OperationalError:
        return None

#Add Individual data to the database
def add_data(table, field, value):
    try:
        query = f'INSERT INTO {table} ({field}) VALUES (?)'

        with closing(conn.cursor()) as c:
            c.execute(query, (value,))
            conn.commit()

    except sqlite3.OperationalError:
        return None

# Add book data to the database
def add_book(title, authorID, publisherID, yearPublished, genreID, loanID):
    try:
        query = '''
                INSERT INTO Books (title, authorID, publisherID, yearPublished, genreID, loanID)
                VALUES(?,?,?,?,?,?)
                '''
        with closing(conn.cursor()) as c:
            c.execute(query, (title, authorID, publisherID, yearPublished, genreID, loanID,))
            conn.commit()

    except sqlite3.OperationalError:
        return None

# Update data in the database
def update_value(table, field, lookup_field, field_value, lookup_value):
    try:
        query = f'UPDATE {table} SET {field} = ? WHERE {lookup_field} = ?'
    
        with closing(conn.cursor()) as c:
            c.execute(query, (field_value, lookup_value,))
            conn.commit()

    except sqlite3.OperationalError:
        return None

# Verify the ID exists and is in the database
def verify_value(table, return_column, lookup_column, value):
    try:
        query = f'SELECT {return_column} FROM {table} WHERE {lookup_column} = ?'

        with closing(conn.cursor()) as c:
            c.execute(query, (value,))
            result = c.fetchone()

            if result:
                actual_value = result[0]
                return actual_value
            
    except sqlite3.OperationalError:
        return None

# Delete a book from the database
def delete_book(bookID):
    try:
        query = '''
                DELETE FROM Books
                WHERE bookID = ?
                '''
        with closing(conn.cursor()) as c:
            c.execute(query, (bookID,))
            conn.commit()
            
    except sqlite3.OperationalError:
        return None

