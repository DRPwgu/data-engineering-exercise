from utils import *
from connection import *
import pandas as pd

pd.set_option('display.max_columns', None)

# Make the connection to the db and get a cursor
try:
    conn = sqlite3.connect('author_books.db')
    c = conn.cursor()
except:
    print('Error connecting to the database, please try later')
    exit()

options()

choice = input('Please make a selection or press "q" to exit: ')

while choice.lower() != 'q':
    if choice == '1':
        author = input('Please enter the name of the author: ')
        author_json = get_author_result(author)

        if author_json['numFound'] == 0:
            print('No result for that author, please verify author\'s name and spelling\n')
        else:
            author_to_enter = query_author(author_json)
            insert_author(c, author_to_enter)
            conn.commit()
            print(author_to_enter)
    elif choice == '2':
        book = input('Please enter the name of the book: ')
        book_json = get_title_result(book)

        if book_json['numFound'] == 0:
            print('No result for this book, please verify book\'s name and spelling')
        else:
            book_to_enter = query_title(book_json)
            a_b = query_authors_books(book_json)

            insert_books(c, book_to_enter)
            insert_authors_books(c, a_b)
            conn.commit()

            print(book_to_enter)
            print(a_b)
    elif choice == '3':
        df = pd.read_sql_query(f'SELECT * from authors', conn)
        print(df)
        print()
    elif choice == '4':
        df = pd.read_sql_query(f'SELECT * from books', conn)
        print(df)
        print()
    elif choice == '5':
        df = pd.read_sql_query(query, conn)
        print(df)
        print()
    elif choice == '6':
        try:
            df = pd.read_sql_query('SELECT * from authors', conn)
            df.to_csv('authors.csv', index=False)
            print('File saved successfully')
        except:
            print('An error occurred writing the file, please try later')
    elif choice == '7':
        try:
            df = pd.read_sql_query('SELECT * from books', conn)
            df.to_csv('books.csv', index=False)
            print('File saved successfully')
        except:
            print('An error occurred writing the file, please try later')
    elif choice == '8':
        try:
            df = pd.read_sql_query(query, conn)
            df.to_csv('authors_books.csv', index=False)
            print('File saved successfully')
        except:
            print('An error occurred writing the file, please try later')
    else:
        print('Please make a valid choice.')

    choice = input('\nPlease make a selection or press "x" to exit: ')
