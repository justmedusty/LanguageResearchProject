# Dustyn Gibb - 040862180

# Import CSV library for reading CSV files
import csv

# full name for being displayed at the top
fullName = "Dustyn Gibb"
# prints full name and separates it from the program output with hyphens
print(fullName)
print("-" * 50)


# method for reading the entirety of the CSV file and just writing a few of the columns into record objects (year,
# prov,vector)
def read_and_print():
    data = open('presentation/data.csv')
    data_read = csv.reader(data)
    year = []
    province = []
    vector = []
    # reads the entire file and then appends values to the 3 predetermined columns declared above
    for record in data_read:
        year.append(record[0])
        province.append(record[1])
        vector.append(record[8])
    # limits the output to 16 so as to be readable
    first_years = year[0:15]
    first_provinces = province[0:15]
    first_vectors = vector[0:15]
    # prints shortened arrays of predetermined values from the CSV file
    for item in first_years:
        print(item)
    for item in first_provinces:
        print(item)
    for item in first_vectors:
        print(item)
    # closing the csv object
    data.close()


# simple try catch calling the method above to read and print the specified values from the csv file, throws error if
# file not found
try:
    read_and_print()
except:
    print("file not found")
