import sqlite3


def db_table_authors_books(c):
    """
    Returns all data on the authors_books table
    :param c:
    :return:
    """
    c.execute("""
        SELECT a.author_id , b.book_id , b.title, a.first_name, a.last_name
        FROM authors as a
        JOIN authors_books ON a.author_id = authors_books.author_id
        JOIN books as b ON b.book_id = authors_books.book_id
    """)
    result = c.fetchall()
    return result


def db_table_authors(c):
    """
    Function returns all data in the authors table
    :param c:
    :return:
    """
    c.execute(""" SELECT * FROM authors """)
    result = c.fetchall()
    return result


def db_table_books(c):
    """
    Function returns all data in the books table
    :param c:
    :return:
    """
    c.execute(""" SELECT * FROM books """)
    result = c.fetchall()
    return result


def insert_author(c, author_data):
    try:
        c.execute("""INSERT INTO authors VALUES( ?,?,?,?,?,?)""", author_data)
    except sqlite3.IntegrityError as e:
        print(e, ' --- AUTHOR ALREADY EXISTS.')


def insert_books(c, books_data):
    try:
        c.execute("""INSERT INTO books VALUES( ?,?,?,?,?)""", books_data)
    except sqlite3.IntegrityError as e:
        print(e, ' --- BOOK ALREADY EXISTS.')


def insert_authors_books(c, authors_books_data):
    try:
        c.execute("""INSERT INTO authors_books VALUES( ?,?)""", authors_books_data)
    except sqlite3.IntegrityError as e:
        print(e, ' --- DATA ALREADY EXISTS.')
