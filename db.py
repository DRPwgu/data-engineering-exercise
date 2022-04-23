"""
Dashel Ruiz Perez 4/16/2022

Run this files independently to make the database and all tables for the project
Right click and choose run db.py

"""

import sqlite3

conn = sqlite3.connect('author_books.db')
c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS authors (
        author_id text PRIMARY KEY,
        first_name text NOT NULL,
        last_name text NOT NULL,
        birth_date text NOT NULL,
        top_work text NOT NULL,
        work_count integer NOT NULL
        )""")

c.execute("""CREATE TABLE IF NOT EXISTS books (
        book_id text PRIMARY KEY,
        title text NOT NULL,
        author_fname text NOT NULL,
        author_lname text NOT NULL,
        first_publish_year text NOT NULL
        )""")

c.execute("""CREATE TABLE IF NOT EXISTS authors_books (
        author_id text NOT NULL,
        book_id text NOT NULL,
        PRIMARY KEY (author_id, book_id),
        FOREIGN KEY(author_id) REFERENCES authors(author_id),
        FOREIGN KEY(book_id) REFERENCES books(book_id)
        )""")

conn.commit()
conn.close()
