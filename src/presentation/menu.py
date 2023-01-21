from business.functionality import Functionality


class Menu:
    def __init__(self):
        pass

    def print_name(self):
        print("Written by Dustyn Gibb")
        return

    def menu(self):
        menu = '''
        Welcome to Practical Project Part 2, Select an option below
        
        1.Reload the data from the dataset, replacing the in-memory data.
        2.Persist the data from memory to the disk as a comma-separated file, writing to a new file.
        3. Select one record
        4. Select multiple records
        5. Create new record and store in memory
        6. Edit a record in memory
        7. Delete a record from memory\n
    
        '''

        print(menu)
        print("-" * 60)
        self.print_name()

    def show_menu(self):
        while True:
            user_action = Functionality()
            self.menu()
            user_choice = input("Insert choice from 1 to 7, press 0 to terminate")
            if user_choice == "0":
                break
            elif user_choice == "1":
                user_action.refresh_memory()
            elif user_choice == "2":
                user_action.write_to_new_file()
            elif user_choice == "3":
                user_action.display_single_record()
            elif user_choice == "4":
                user_action.display_many_records()
            elif user_choice == "5":
                user_action.create_record()
            elif user_choice == "6":
                user_action.edit_record()
            elif user_choice == "7":
                user_action.delete_record()
            else:
                print("invalid input")
