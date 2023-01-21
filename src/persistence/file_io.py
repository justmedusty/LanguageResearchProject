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

    :param filename: the csv file passed in
    :return: the file to be read
    """
    file_to_read = csv.reader(filename)
    return file_to_read


def close_file(filename):
    filename.close()


def load_records(filename):
    records = []

    for record in filename:
        if len(records) < 100:
            records.append(record)
    return records
