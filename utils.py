import requests


def get_author_result(author):
    """
    Receive string (author name) as an argument and return the api response as a json file.
    If the response is not successful (200) returns an exception
    :param author:
    :return:
    """
    result = requests.get(f'https://openlibrary.org/search/authors.json?q={author}')
    if result.status_code == 200:
        return result.json()
    else:
        raise Exception('Error downloading API response')


def get_title_result(title):
    """
    Receive string (book title) as an argument and return the api response as a json file.
    If the response is not successful (200) returns an exception
    :param title:
    :return:
    """
    result = requests.get(f'https://openlibrary.org/search.json?title={title}')
    if result.status_code == 200:
        return result.json()
    else:
        raise Exception('Error downloading API response')


def query_author(json_data):
    """
    Receive json data as an argument and returns a tuple for entering data on the authors DB
    :param json_data:
    :return:
    """
    author_id = json_data['docs'][0]['key']
    full_name = json_data['docs'][0]['name'].split()
    f_name = full_name[0]
    l_name = full_name[1]
    b_date = json_data['docs'][0]['birth_date']
    t_work = json_data['docs'][0]['top_work']
    w_count = json_data['docs'][0]['work_count']

    query_tuple = (author_id, f_name, l_name, b_date, t_work, w_count)

    return query_tuple


def query_title(json_data):
    """
    Receive json data as an argument and returns a tuple for entering data on the books DB
    :param json_data:
    :return:
    """
    book_id = json_data['docs'][0]['key'][7:]
    title = json_data['docs'][0]['title']
    f_year_pub = json_data['docs'][0]['first_publish_year']
    author_name = json_data['docs'][0]['author_name'][0].split()
    author_f_name = author_name[0]
    author_l_name = author_name[1]

    result = (book_id, title, author_f_name, author_l_name, f_year_pub)
    return result


def query_authors_books(json_data):
    """
    Receive json data as an argument and returns a tuple for entering data on the authors_books DB
    :param json_data:
    :return:
    """
    author_key = json_data['docs'][0]['author_key'][0]
    book_id = json_data['docs'][0]['key'][7:]

    result = (author_key, book_id)
    return result


def options():
    print('\nThis is a Pipeline application to enter data in the authors books DB')
    print('Please read all the choices before making a selection')
    print('1 - Enter data in the Authors table')
    print('2 - Enter data in the Books table')
    print('3 - Print the data in the Authors table')
    print('4 - Print the data in the Books table')
    print('5 - Print the data in the Authors_Books table')
    print('6 - Save the data in the Authors table as a CSV file')
    print('7 - Save the data in the Books table as a CSV file')
    print('8 - Save the data in the Authors_Books table as a CSV file\n')
