from utils import *
from connection import *
import pandas as pd
pd.set_option('display.max_columns', None)

# Make the connection to the db and get a cursor
conn = sqlite3.connect('author_books.db')
c = conn.cursor()

options()

choice = input('Please make a selection or press "x" to exit: ')

while choice != 'x':
    if choice == '1':
        author = input('Please enter the name of the author: ')
        author_json = get_author_result(author)
        if author_json['numFound'] == 0:
            print('No result for that author, please check the spelling\n')
        else:
            author_to_enter = query_author(author_json)
            insert_author(c, author_to_enter)
            conn.commit()
    elif choice == '2':
        pass
    elif choice == '3':
        df = pd.read_sql_query(f'SELECT * from authors', conn)
        print(df)
        print()
    elif choice == '4':
        df = pd.read_sql_query(f'SELECT * from books', conn)
        print(df)
        print()
    elif choice == '5':
        df = pd.read_sql_query(f'SELECT * from authors_books', conn)
        print(df)
        print()
    elif choice == '6':
        pass
    elif choice == '7':
        pass
    elif choice == '8':
        pass
    else:
        print('Please make a valid choice.')

    choice = input('Please make a selection or press "x" to exit: ')
