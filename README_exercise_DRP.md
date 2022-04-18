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
* First, I read the exercise several times to understand the problem.
* After that, I went to the web page links provided in the ReadMe file inside the GitHub repository.
* I played with the API on the browser to understand how the response was formatted and structure the JSON response I was going to receive.
* After that, I went back to the readme file. 
* Do as little or as much as you like.
* Writing a Python program to get API requests is not that hard. I decided to use the requests library because it is easy to use; it just needs a pip install.
* I thought that the crucial part of the exercise was the design of the tables inside the DB.
* I could write CSV files with all the data inside a DB table using the pandas library.
* I thought that the best idea was to make a DB because finding duplicates in a CSV file would be more complicated than making a DB.
* I needed to make a table design anyways, and sqlite3 could make everything easier and better.
* I could add primary keys to enforce uniqueness and avoid duplicates in my data.
* I decided to make the three tables the exercise asked for, a table for authors, books, and the union of authors and books. 
* The authors_books table was going to be used as a bridge due to a many-to-many relationship, an author can write many books, and a book can be written by many authors. 
## Here is the DDL for my table in the DB
```
CREATE TABLE authors (
    author_id text PRIMARY KEY,
    first_name text NOT NULL,
    last_name text NOT NULL,
    birth_date text NOT NULL,
    top_work text NOT NULL,
    work_count integer NOT NULL
    )
```



# Additional Info:
* we expect that this will take you a few hours to complete
* use any langugage or framework you are comfortable with we prefer Python
* Bonus points for setting up a db
* Bonus points for security, specs, etc.
* Do as little or as much as you like.

Please fork this repo and commit your code into that fork. Show your work and process through those commits.





