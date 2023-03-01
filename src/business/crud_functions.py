# This class is used to create, read, update, and delete data from a list.
class CrudFunctions:
    def __init__(self):
        pass

    def create_record(self, data, record):
        """
        It takes a list of data and a record, and appends the record to the list

        :param data: the list of records
        :param record: a dictionary of the record to be created
        :return: The data list is being returned.
        """
        data.append(record)
        return data

    def update_record(self, data, row, column, new_value):
        """
        It takes a list, a row number, a column number, and a new value, and returns the list of lists with the new
        value in the specified row and column

        :param data: the data you want to update
        :param row: The row number of the record to update
        :param column: The column number of the cell you want to update
        :param new_value: The new value to be inserted into the table
        :return: The data is being returned.
        """
        data[row - 1][column - 1] = new_value
        return data

    def delete_record(self, data, row):
        """
        It deletes a record from the data list

        :param data: the list of lists that contains the data
        :param row: The row number of the record to be deleted
        :return: The data is being returned.
        """
        del data[row - 1]
        return data
