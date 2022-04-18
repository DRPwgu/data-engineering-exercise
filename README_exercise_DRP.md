# Fender Digital Data Engineering Exercise

Design and implement a data pipeline that that pulls data about books and authors for a topic you are interested in using [Open Library.](https://openlibrary.org/developers/api) It is suggested that you leverage the [search api](https://openlibrary.org/dev/docs/api/search) to limit your results. As an output of this exercise we expect to see a minimum of the following:

1. Python program that pulls data from the rest api
2. CSV files for the following:
	* Authors
	* Books
	* Authors and Books (a bridge table between the previous entities)
3. DDL to create a hypothetical database schema ( you don't have to create a DB but you are welcome to)

The objective of this exercise is to have you walk us through a solution you have created. Do as much or as little as you would like.


# ReadMe
First, I read the exercise several times to understand the problem.
After that, I went to the web page links provided in the ReadMe file inside the GitHub repository. 
I played with the API on the browser to understand how the response was formatted and structure the JSON response I was going to receive.
After that, I went back to the readme file. 
Writing a Python program to get API requests is not that hard. I decided to use the requests library because it is easy to use; it just needs a pip install.
 I thought that the crucial part of the exercise was the design of the tables inside the DB. I could write CSV files with all the data inside a DB table using the pandas library. 
I thought that the best idea was to make a DB because finding duplicates in a CSV file would be more complicated than making a DB. I needed to make a table design anyways, and sqlite3 could make everything easier and better. I could add primary keys to enforce uniqueness and avoid duplicates in my data.
I decided to make the three tables the exercise asked for, a table for authors, books, and the union of authors and books. 
The authors_books table was going to be used as a bridge due to a many-to-many relationship, an author can write many books, and a book can be written by many authors. 
Here is the DDL for my table in the DB
CREATE TABLE authors (
    author_id text PRIMARY KEY,
    first_name text NOT NULL,
    last_name text NOT NULL,
    birth_date text NOT NULL,
    top_work text NOT NULL,
    work_count integer NOT NULL
    )
CREATE TABLE books (
    book_id text PRIMARY KEY,
    title text NOT NULL,
    author_fname text NOT NULL,
    author_lname text NOT NULL,
    first_publish_year text NOT NULL
    )
CREATE TABLE authors_books (
    author_id text NOT NULL,
    book_id text NOT NULL,
    PRIMARY KEY (author_id, book_id),
    FOREIGN KEY(author_id) REFERENCES authors(author_id),
    FOREIGN KEY(book_id) REFERENCES books(book_id)
    )
I used the authors' and book's keys in the response as the primary key for each table because those were unique. 
Use the combination of those keys as a primary key for the bridge table to avoid duplicates.
Lastly, clone the repository, open the folder in PyCharm, and get to work.

To run the project first needs to be cloned on the local machine. The project was done using PyCharm. 
Open PyCharm, make a new project and use the folder you cloned as the new project's location. Run the requirements.txt file to get all dependencies. 
If you want to make a new DB, you can manually delete the authors_books.db file and run the db.py file inside the project(this file will make a new DB empty)

The program is a command-line application that gives you several options. You can do as many instructions as you want until you press q to quit the program.
The app enters authors and books one at a time. 
Ex. of the options:
Please make a selection or press "q" to exit
1 - Enter data in the Authors table
2 - Enter data in the Books table
3 - Print the data in the Authors table
4 - Print the data in the Books table
5 - Print the data in the Authors_Books table
6 - Save the data in the Authors table as a CSV file
7 - Save the data in the Books table as a CSV file
8 - Save the data in the Authors_Books table as a CSV file

The next feature is to use a txt file or a list to enter several authors and several books. 
Will be great if I make it possible to make simple queries to the DB.

I enjoyed doing the exercise; the directions were clear and easy to understand. One recommendation could maybe be using a template for the readme explanation, and another is giving the person doing the exercise an empty DB (Postgres, MySQL) to finish the exercise. 




# Additional Info:
* we expect that this will take you a few hours to complete
* use any langugage or framework you are comfortable with we prefer Python
* Bonus points for setting up a db
* Bonus points for security, specs, etc.
* Do as little or as much as you like.

Please fork this repo and commit your code into that fork. Show your work and process through those commits.





