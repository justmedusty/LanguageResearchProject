import csv

file = 'data.csv'


def open_file(filename):
    try:
        opened_file = open(filename)
        return opened_file
    except FileNotFoundError:
        print("Error: File not found")


def read_file(filename):
    file_to_read = csv.reader(file)
    return file_to_read


def close_file(filename):
    filename.close()


def load_records(filename):
    records = []

    for record in filename:
        if len(filename) < 100:
            records.append(record)
    return records
