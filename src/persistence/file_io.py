import csv

file = '../presentation/data.csv'


def open_file(filename):
    """
    Utilizes CSV api to read a csv file and return the opened file
    :param filename: the csv file to be read
    :return: the opened file
    """
    try:
        opened_file = open(filename)
        return opened_file
    except FileNotFoundError:
        print("Error: File not found")


def read_file(filename):
    """
    Utilizes the reader of csv library to read a file
    :param filename: the csv file passed in
    :return: the file to be read
    """
    file_to_read = csv.reader(filename)
    return file_to_read


def close_file(filename):
    """
    closes an open file
    :param filename: the csv file passed
    """
    filename.close()


def load_records(filename):
    """
    loads all of the records in the csv file into a list
    :param filename: csv file
    :return: records stored in the file
    """
    records = []

    for record in filename:
        if len(records) < 100:
            records.append(record)
    return records


def load_column_headers(filename):
    """
    This function takes a filename as an argument and returns a list of column headers.

    :param filename: the name of the file you want to open
    :return: The column headers are being returned.
    """
    column_headers = []
    for record in filename:
        counter = 0
        if counter < 1:
            column_headers.append(record)
    return column_headers
