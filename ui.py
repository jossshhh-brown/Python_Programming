#!/usr/bin/env python3

'''
BookNook app - written by Josh Brown
This app will allow the user to enter details about their library
of books as well as make updates to individual pieces, or an overall book.
They will also be able to keep track of which books are on loan. A sample book
is provided. 
'''

import db
from business import Book

def display_divider() -> str:
    '''
    Used to print the divider between various display objects
    '''
    print('=' * 80)
    
def display_title() -> str:
    '''
    Used to display the title of the app in the main menu
    '''
    print('\t\t\t\tWelcome to \'BookNook\'')
    print()

def display_menu() -> str:
    '''
    Used to display the menu options available for the user 
    '''
    print('MENU OPTIONS')
    print()
    print('View Options:')
    print('1. View all Books')
    print('2. View all Loaned Books')
    print('3. View all Authors')
    print('4. View all Genres')
    print('5. View all Publishers')
    print()
    print('Add Options:')
    print('6. Add a Book')
    print('7. Add an Author')
    print('8. Add a Publisher')
    print('9. Add a Genre')
    print()
    print('Update Options:')
    print('10. Update a Book')
    print('11. Update an Author')
    print('12. Update a Publisher')
    print('13. Update a Genre')
    print('14. Update Loan Status')
    print()
    print('General Options:')
    print('15. Show Menu')
    print('16. Exit Program')
    print()

def display_books(book_list) -> str:
    '''
    Used to provide a list of books that have been saved and the details for
    each book
    '''
    if book_list == None:
        print('Nothing to display')
    else:
        print()
        print('\t\t\t\t***BOOKS***')
        print()
        print('\tBook Details')
        display_divider()
        for book in book_list:
            bookID, title, author, publisher, year_published, genre, on_loan = book.book_setList()
            print(f'''{bookID}\t\'{title}\' by {author}
                  Genre ............. {genre}
                  Year Published .... {year_published}
                  Publisher ......... {publisher}
                  ''')
    print()

def display_loaned_books(loaned_list) -> str:
    '''
    Used to provide a list of books that are on loan as well as the details
    for that book
    '''
    if loaned_list == None:
        print('Nothing to display')
    else:
        print()
        print('\t\t\t\t***LOANED BOOKS***')
        print()
        print('\tBook details')
        display_divider()
        for loan in loaned_list:
            bookID, title, author, publisher, year_published, genre, on_loan = loan.book_setList()
            print(f'''{bookID}\t\'{title}\' by {author}
                  Genre ............. {genre}
                  Year Published .... {year_published}
                  Publisher ......... {publisher}
                  ''')
            print()
    print()

def display_authors(authors) -> str:
    '''
    Used to provide a list of authors in the library 
    '''
    if authors == None:
        print('Nothing to display')
    else:
        print()
        print('\t\t\t\t***AUTHORS***')
        print()
        print('\tAuthor')
        display_divider()
        for author in authors:
            authorID, name = author.auth_setList()
            print(f'{authorID}\t{name}')
    print()  

def display_genres(genres) -> str:
    '''
    Used to provide a list of genres in the library
    '''
    if genres == None:
        print('Nothing to display')
    else:
        print()
        print('\t\t\t\t***GENRES***')
        print()
        print('\tGenre')
        display_divider()
        for genre in genres:
            genreID, genre = genre.gen_setList()
            print(f'{genreID}\t{genre}')
    print()

def display_publishers(publishers) -> str:
    '''
    Used to provide a list of publishers in the library
    '''
    if publishers == None:
        print('Nothing to display')
    else:
        print()
        print('\t\t\t\t***PUBLISHERS***')
        print()
        print('\tPublisher')
        display_divider()
        for publisher in publishers:
            publisherID, name = publisher.pub_setList()
            print(f'{publisherID}\t{name}')
    print()  

def add_item(db_list, authors, publishers, genres, book_list) -> str:
    '''
    Used to add an author, publisher, genre, or book to the data
    '''
    while True:
         
        if db_list == authors: # adds a new author based on input from the user.
            new_item = input('Confirm add new Author? (Y/N)\t').lower()
            print()
            if new_item == 'n':
                print('Add request cancelled.')
                print()
                break
            elif new_item == 'y': # Returns the author name for use in other functions
                new_item = input('Please enter the new author here:\t')
                print()
                db.add_data('Authors', 'name', new_item)
                print(f'{new_item} has been added.')
                print()
                return new_item
                break
            else:
                print('Please make a valid selection. (Y/N)')
                print()
        elif db_list == publishers: # adds a new publisher based on input from the user.
            new_item = input('Confirm add new Publisher? (Y/N) ').lower()
            print()
            if new_item == 'n':
                print('Add request cancelled.')
                print()
                break
            elif new_item == 'y': # Returns the publisher name for use in other functions
                new_item = input('Please enter the new publisher here:\t')
                print()
                db.add_data('Publishers', 'name', new_item)
                print(f'{new_item} has been added.')
                print()
                return new_item
                break
            else:
                print('Please make a valid selection. (Y/N)')
                print()
        elif db_list == genres: # adds a new genre based on input from the user.
            new_item = input('Confirm Add new Genre? (Y/N)\t').lower()
            print()
            if new_item == 'n':
                print('Add request cancelled.')
                print()
                break
            elif new_item == 'y': # Returns the genre name for use in other functions
                new_item = input('Please enter the new genre here:\t')
                print()
                db.add_data('Genres', 'genre', new_item)
                print(f'{new_item} has been added.')
                print()
                return new_item
                break
            else:
                print('Please make a valid selection. (Y/N)')
                print()
        elif db_list == book_list: # adds a new book based on input from the user.
            display_books(book_list)
            new_item = input('Is the book already in this list? (Y/N)\t').lower()
            print()
            if new_item == 'y':
                print('Add request cancelled.')
                print()
                break
            elif new_item == 'n':
                book_title = input('Please enter the book title:\t ')
                print()
                book_year = int(input('Please enter the year of publishing:\t'))
                print()

                # Display current authors, publishers and genres for use in the following sections
                display_authors(authors)
                display_publishers(publishers)
                display_genres(genres)

                # Check if the user wants to add a new author and take appropriate actions
                user_check = input('Would you like to enter a new author? (Y/N)\t').lower()
                print()
                if user_check == 'y':
                    new_author = add_item(authors, authors, publishers, genres, book_list)
                    authors = db.get_author()
                    book_author = db.verify_value('Authors', 'authorID', 'name', new_author)
                elif user_check == 'n':
                    book_author = int(input('Please select the number for the author from the chart above:\t'))
                    print()

                # Check if the user wants to add a new publisher and take appropriate actions
                user_check = input('Would you like to enter a new publisher? (Y/N)\t').lower()
                print()
                if user_check == 'y':
                    new_publisher = add_item(publishers, authors, publishers, genres, book_list)
                    publishers = db.get_publisher()
                    book_publisher = db.verify_value('Publishers', 'publisherID', 'name', new_publisher)
                elif user_check == 'n':
                    book_publisher = int(input('Please select the number for the publisher from the chart above:\t'))
                    print()

                # Check if the user wants to add a new genre and take appropriate actions    
                user_check = input('Would you like to enter a new genre? (Y/N)\t').lower()
                print()
                if user_check == 'y':
                    new_genre = add_item(genres, authors, publishers, genres, book_list)
                    genres = db.get_genre()
                    book_genre = db.verify_value('Genres', 'genreID', 'genre', new_genre)
                elif user_check == 'n':
                    book_genre = int(input('Please select the number for the genre from the chart above:\t'))
                    print()
                    
                # Sets the default loan value to "False"
                book_loan = 2

                # add the book to the database based on user input, and provide feedback that the book was added
                db.add_book(book_title, book_author, book_publisher, book_year, book_genre, book_loan)
                print()
                print(f'\'{book_title}\' has been added.')
                print()
                break
            else:
                print('Please make a valid selection. (Y/N)')
                print()
        else:
            print('Invalid selection, please try again.')
            print()

def update_item(db_list, authors, publishers, genres, book_list, loaned_list) -> str:
    '''
    Used to update an author, publisher, genre, book or loan status in the library
    '''
    while True:
        if db_list == authors: # update the author based on user input
            display_authors(authors)
            user_selection = int(input('Please enter the number for the author to update:\t'))
            print()
            user_check = db.verify_value('Authors', 'name', 'authorID', user_selection)
            confirm = input(f'You chose {user_check}, is that correct? (Y/N)\t').lower()
            print()
            if confirm == 'y':
                new_value = input('Please enter the updated Author Name:\t')
                print()
                db.update_value('Authors', 'name', 'authorID', new_value, user_selection)
                authors = db.get_author()
                print(f'Author updated to {new_value}')
                print()
                break
            elif confirm == 'n':
                # if the author is not the one the user intended to select, cirlce back to the beginning
                update_item(authors, authors, publishers, genres, book_list, loaned_list)
            else:
                print('Please enter a valid option (Y/N)')
                print()
                break
        elif db_list == publishers: # update a publisher based on user input
            display_publishers(publishers)
            user_selection = int(input('Please enter the number for the publisher to update:\t'))
            print()
            user_check = db.verify_value('Publishers', 'name', 'publisherID', user_selection)
            confirm = input(f'You chose {user_check}, is that correct? (Y/N)\t').lower()
            print()
            if confirm == 'y':
                new_value = input('Please enter the updated Publisher Name:\t')
                print()
                db.update_value('Publishers', 'name', 'publisherID', new_value, user_selection)
                publishers = db.get_publisher()
                print(f'Publisher updated to {new_value}')
                print()
                break
            elif confirm == 'n':
                # if the publisher is not the one the user intended to select, cirlce back to the beginning
                update_item(publishers, authors, publishers, genres, book_list, loaned_list)
            else:
                print('Please enter a valid option (Y/N)')
                print()
                break
        elif db_list == genres: # update a genre based on user input
            display_genres(genres)
            user_selection = int(input('Please enter the number for the genre to update:\t'))
            print()
            user_check = db.verify_value('Genres', 'genre', 'genreID', user_selection)
            confirm = input(f'You chose {user_check}, is that correct? (Y/N)\t').lower()
            print()
            if confirm == 'y':
                new_value = input('Please enter the updated genre:\t')
                print()
                db.update_value('Genres', 'genre', 'genreID', new_value, user_selection)
                genres = db.get_genre()
                print(f'Genre updated to {new_value}')
                print()
                break
            elif confirm == 'n':
                # if the genre was not the intended genre, circle back to the beginning
                update_item(genres, authors, publishers, genres, book_list, loaned_list)
            else:
                print('Please enter a valid option (Y/N)')
                print()
                break
        elif db_list == loaned_list: # update the loaned status on a book (add or remove)
            add_or_remove = input('Would you like to add or remove a loan? (A/R)\t').lower()
            print()
            if add_or_remove == 'a': # processes if the user wishes to add a loan
                display_books(book_list)
                user_selection = int(input('Please enter the number for the book to update:\t'))
                print()
                user_check = db.verify_value('Books', 'title', 'bookID', user_selection)
                confirm = input(f'You chose {user_check}, is that correct? (Y/N)\t').lower()
                print()
                if confirm == 'y':
                    new_value = 1
                    db.update_value('Books', 'loanID', 'bookID', new_value, user_selection)
                    book_list = db.get_all_books()
                    loaned_list = db.get_loaned_books()
                    print(f'Loan added to {user_check}')
                    print()
                    break
                elif confirm == 'n':
                    # if the book chosen was not the intended book, circle back to the beginning
                    update_item(loaned_list, authors, publishers, genres, book_list, loaned_list)
                else:
                    print('Please enter a valid option (Y/N)')
                    print()
                    break
            elif add_or_remove == 'r': # processes if the user wishes to remove a loan
                display_loaned_books(loaned_list)
                user_selection = int(input('Please enter the number for the book to update:\t'))
                print()
                user_check = db.verify_value('Books', 'title', 'bookID', user_selection)
                confirm = input(f'You chose {user_check}, is that correct? (Y/N)\t').lower()
                print()
                if confirm == 'y':
                    new_value = 2
                    db.update_value('Books', 'loanID', 'bookID', new_value, user_selection)
                    book_list = db.get_all_books()
                    loaned_list = db.get_loaned_books()
                    print(f'Loan removed from {user_check}')
                    print()
                    break
                elif confirm == 'n':
                    # if the book chosen was not the intended book, circle back to the beginning
                    update_item(loaned_list, authors, publishers, genres, book_list, loaned_list)
                else:
                    print('Please enter a valid option (Y/N)')
                    print()
                    break
        elif db_list == book_list: # updates the data by deleting the selected book and running the "add" function
            display_books(book_list)
            user_selection = int(input('Please enter the number for the book to update:\t'))
            print()
            user_check = db.verify_value('Books', 'title', 'bookID', user_selection)
            confirm = input(f'You chose {user_check}, is that correct? (Y/N)\t').lower()
            print()
            if confirm == 'y':
                db.delete_book(user_selection)
                print(f'Book {user_check} has been removed and we will now replace it with new data')
                print()
                book_list = db.get_all_books()
                add_item(book_list, authors, publishers, genres, book_list)
                break
            elif confirm == 'n':
                # if the book chosen was not the intended book, circle back to the beginning
                update_item(book_list, authors, publishers, genres, book_list, loaned_list)
            else:
                print('Please enter a valid option (Y/N)')
                print()
                break

def main():
    # Set up the menu for the user 
    display_divider()
    display_title()
    display_menu()
    display_divider()

    # Connect to the database
    db.connect_db()
    
    # Populate the lists from each of the tables in the database
    book_list = db.get_all_books()
    if book_list == None:
        book_list = Book.book_setList()
        
    loaned_list = db.get_loaned_books()
    if loaned_list == None:
        loaned_list = Loan.loan_setList()
        
    publishers = db.get_publisher()
    if publishers == None:
        publishers = Publisher.pub_setList()
        
    authors = db.get_author()
    if authors == None:
        autohrs = Author.auth_setList()
        
    genres = db.get_genre()
    if genres == None:
        genres = Genre.gen_setList()
        
    loans = db.get_loan()
    if loans == None:
        loans = Loan.loan_setList()

    # Control the flow of the program based on user input
    while True:
        option = input('Please enter a menu option:\t')
        if int(option) == 1:
            book_list = db.get_all_books()
            display_books(book_list)
        elif int(option) == 2:
            loaned_list = db.get_loaned_books()
            display_loaned_books(loaned_list)
        elif int(option) == 3:
            authors = db.get_author()
            display_authors(authors)
        elif int(option) == 4:
            genres = db.get_genre()
            display_genres(genres)
        elif int(option) == 5:
            publishers = db.get_publisher()
            display_publishers(publishers)
        elif int(option) == 6:
            book_list = db.get_all_books()
            add_item(book_list, authors, publishers, genres, book_list)
        elif int(option) == 7:
            authors = db.get_author()
            add_item(authors, authors, publishers, genres, book_list)
        elif int(option) == 8:
            publishers = db.get_publisher()
            add_item(publishers, authors, publishers, genres, book_list)
        elif int(option) == 9:
            genres = db.get_genre()
            add_item(genres, authors, publishers, genres, book_list)
        elif int(option) == 10:
            book_list = db.get_all_books()
            update_item(book_list, authors, publishers, genres, book_list, loaned_list)
        elif int(option) == 11:
            authors = db.get_author()
            update_item(authors, authors, publishers, genres, book_list, loaned_list)
        elif int(option) == 12:
            publishers = db.get_publisher()
            update_item(publishers, authors, publishers, genres, book_list, loaned_list)
        elif int(option) == 13:
            genres = db.get_genre()
            update_item(genres, authors, publishers, genres, book_list, loaned_list)
        elif int(option) == 14:
            loaned_list = db.get_loaned_books()
            update_item(loaned_list, authors, publishers, genres, book_list, loaned_list)
        elif int(option) == 15:
            display_menu()
        elif int(option) == 16:
            print()
            print('Bye!')
            break
        else:
            print()
            print('Please choose a different option')
            print()
                
# Start the program at the main() function
if __name__ == '__main__':
    main()
