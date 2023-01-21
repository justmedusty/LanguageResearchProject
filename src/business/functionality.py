import csv

import persistence.file_io
from business.create_record import CreateRecord


class Functionality:
    total_records = 0

    def __init__(self):
        """
        This function opens a file, reads the file, loads the records from the file, and closes the file
        """
        file = persistence.file_io.file
        open_file = persistence.file_io.open_file(file)
        read_file = persistence.file_io.read_file(open_file)
        self.memory_bank = persistence.file_io.load_records(read_file)
        persistence.file_io.close_file(open_file)

    def refresh_memory(self):
        """
        This function prints out the contents of the memory bank, and then prints out the total number of records in the
        memory bank
        :return: The memory bank is being returned.
        """
        for record in self.memory_bank:
            print(record)
            self.total_records = len(self.memory_bank)
        print(self.total_records)
        return self.memory_bank

    def create_record(self):
        """
        The function takes in user input and creates a new record object, which is then appended to the memory bank
        some fields left out for simplicity
        """

        ref_date = input("Enter ref date")
        geo = input("Enter province")
        dguid = "2016AFDF34"
        area = input("enter type of area")
        uom = input("Enter units of measurement")
        uom_id = 123
        scalar_factor = "thousands"
        scalar_id = 0
        vector = "v43443"
        coordinate = 1.1
        value = input("enter value (int or double")
        status = ""
        symbol = ""
        terminated = ""
        decimals = 0

        new_record = CreateRecord.create_record(self, ref_date, geo, dguid, area, uom, uom_id, scalar_factor, scalar_id,
                                                vector,
                                                coordinate,
                                                value,
                                                status, symbol, terminated, decimals)
        self.memory_bank.append(new_record)
        print(new_record)
        print("Successfully added new record")

    def write_to_new_file(self):
        """
        It opens a new file, writes the contents of the memory bank to the new file, and then closes the file
        :return: True
        """
        output_path = "new-file.csv"
        with open(output_path, 'w') as output_file:
            writer = csv.writer(output_file)
            writer.writerows(self.memory_bank)
            print("File has been written")
            return True

    def display_single_record(self):
        """
        This function takes a record number as input and displays the record at that index in the memory bank
        """
        record_number = int(input("Enter record number to show"))
        index = record_number - 1
        if record_number <= len(self.memory_bank):
            print(self.memory_bank[record_number])
        else:
            print("Invalid record number")

    def delete_record(self):
        """
        This function deletes a record from the memory bank
        """

        while True:
            record_row = int(input("Enter record index to delete said record"))
            if record_row <= len(self.memory_bank):
                record_row = record_row - 1
                print(self.memory_bank[record_row])
                del self.memory_bank[record_row]
                print("Deleted")
                return


            else:
                print("Invalid record number")

    def edit_record(self):
        """
        This function allows the user to edit a record in the memory bank
        :return: the value of the record that was edited.
        """
        while True:
            record_row = int(input("Enter row number to edit"))
            if record_row <= len(self.memory_bank):
                record_row = record_row - 1
                record_column = int(input("Enter the column number to edit"))
                if record_column <= len(self.memory_bank[record_row]):
                    record_column = record_column - 1
                    print(self.memory_bank[record_row][record_column])
                    new_record_value = input("Enter new record value")
                    self.memory_bank[record_row][record_column] = new_record_value
                    print(self.memory_bank[record_row][record_column])
                    print("Updated")
                    return

                else:
                    print("invalid number")
            else:
                print("invalid row value")

    def display_many_records(self):
        """
        This function takes in a number from the user and displays that number of records from the memory bank
        :return: A list of the records that were displayed.
        """
        number_to_show = (int(input("Type number of records to display")))
        my_list = []
        counter = 0
        while counter < number_to_show:
            my_list.append(self.memory_bank[counter])
            counter += 1
        else:
            print("Invalid number")
        for item in my_list:
            print(item)
        return my_list
