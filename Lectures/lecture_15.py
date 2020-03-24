import csv

# Lecture 15 objectives

# 01. Read from and write to files
# 02. Use with statement and built-in open() function
# 03. Work with *.txt and *.csv files (use csv module)
# 04. Write filtered data to file.


# PYTHON FILE OBJECT METHODS
# https://www.w3schools.com/python/python_ref_file.asp

# CONSTANTS
WHALE_NAMES = 'whale_names.txt'
NOAA_WHALES = 'noaa_whales.csv'


# 1.0 READING/WRITING FILES: YE OLDE WAY

print('\n') # padding

# 1.1 CREATE FILE OBJECT, RETURN LIST USING read() METHOD
file_obj = open(WHALE_NAMES) # open
data = file_obj.read()
file_obj.close() # close (REQUIRED)

print(f"data type={type(data)}\n") # read() returns a string
print(f"read()\n{data}\n")


# 1.2 CREATE FILE OBJECT, RETURN LIST USING readline() METHOD

# open(): optional parameter modes

# 'r': read
# 'w': write
# 'x': create, write (new file)
# 'a': append (to existing file)
# 'r+': read, write (to same file)

# file_obj = open('some path', 'r') # read mode
# file_obj = open('some path', 'w') # write mode

file_obj = open(WHALE_NAMES, 'r') # open
data = file_obj.readline()
# data += file_obj.readline() # UNCOMMENT: can call n times but not efficient
file_obj.close() # close (REQUIRED)

print(f"readline()\n{data}\n")


# 1.3 CREATE FILE OBJECT, RETURN LIST USING readlines() METHOD
file_obj = open(WHALE_NAMES, 'r') # open
data = file_obj.readlines()
file_obj.close() # close (REQUIRED)

print(f"data type={type(data)}\n") # readlines() returns a list
print(f"readlines()\n{data}\n") # prints a list (note trailing \n)
print(f"readlines(), join()\n{''.join(data)}\n") # print string (pretty)


# 1.4 Gotcha: CREATE FILE OBJECT, CALL read(), readlines()
# read(), readlines() limited to one call only
file_obj = open(WHALE_NAMES, 'r') # open
data = file_obj.read()
data_lines = file_obj.readlines() # does not execute
file_obj.close() # close (REQUIRED)

print(f"data_lines list is empty = {data_lines}\n")


# 1.5 ALTERNATIVE: LOOP OVER FILE OBJECT, LINE BY LINE
data = []
file_obj = open(WHALE_NAMES, 'r') # open
for line in file_obj:
    data.append(line)
file_obj.close() # close (REQUIRED)

print(f"loop over file_obj = {data}\n")


# 1.6 WRITE TO FILE WITH writelines()
path = 'whale_names_out_1.txt'
file_obj = open(path, 'w')
file_obj.writelines(data)
file_obj.close() # close (REQUIRED)


# 1.7 WRITE TO FILE WITH write()
path = 'whale_names_out_2.txt'
file_obj = open(path, 'w')
for row in data:
    file_obj.write(row)
file_obj.close() # close (REQUIRED)



# 2.0 READING/WRITING FILES: WITH STATEMENT (PREFERRED)

# 2.1 READ FILE USING with open()

def read_file(path):
    """TODO"""

    data = []
    with open(path, 'r', encoding='utf-8') as file_obj:
        for row in file_obj:
            data.append(row)

    return data


# Call function
data = read_file(WHALE_NAMES)

print(f"With statement: loop over file_obj\n{data}\n") # note trailing \n
print(f"With statement: loop over file_obj\n{''.join(data)}\n")


# 2.2 WRITE TO FILE USING with open() AND writelines()
def write_file(path, data):
    """TODO"""
    with open(path, 'w', encoding='utf-8') as file_obj:
        file_obj.writelines(data)


# Call function (if file does not exist it will be created)
path = 'whale_names_out_3.txt'
write_file(path, data)


# 2.3 WRITE TO FILE USING with open() AND write()
# Loop over data rows in order to add number to row
def write_file_write(path, data):
    """TODO"""
    with open(path, 'w', encoding='utf-8' ) as file_obj:
        for i, row in enumerate(data, 1):
            file_obj.write(f"{i}. {row}")


# Call function (if file does not exist it will be created)
path = 'whale_names_out_4.txt'
write_file_write(path, data)


# 2.4 REFORMAT LIST DATA AS STRING
def convert_to_str(data):
    """TODO"""
    string = ''
    for i, row in enumerate(data, 1):
        string += f"{i}. {row}"

    return string


# Call function and write to file
data_str = convert_to_str(data) # one task only
write_file(path, data_str) # one task only (generic)



# 3.0 READING/WRITING CSV FILES

# Import csv module (see above)
# Create csv reader/writer objects
# Access appropriate methods

# 3.1 READ CSV FILE WITH csv.reader()
def read_csv(path, delimiter=','):
    """TODO"""

    data = []

    with open(path, 'r', newline='', encoding='utf-8') as csv_file:
        reader = csv.reader(csv_file, delimiter=delimiter)
        for row in reader:
            data.append(row)

        return data


# Call function
data = read_csv(NOAA_WHALES)

print(f"NOAA csv data = {data}\n")


# 3.2 WRITE TO CSV FILE USING csv.writer()
def write_csv(path, data):
    """TODO"""
    with open(path, 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(data) # iterable

        # for row in data:
        #     writer.writerow(row)

# Call function
path = 'noaa_whales_out_1.csv'
write_csv(path, data)



# 4.0 WHALE DATA EXERCISE: WRITE FILTERED DATA TO FILE

# 4.1 FILTER ON BALEEN WHALES

# Read file
whales = read_csv(NOAA_WHALES)
columns = whales[0] # extract column names

# Prep list
baleen_whales = [columns] # add column names as first row

for whale in whales[1:]:
    if whale[columns.index('type')] == 'Mysticeti (Baleen)':
        baleen_whales.append(whale)

# Write to file
path = 'noaa_whales_baleen.csv'
write_csv(path, baleen_whales)


# 4.2 FILTER ON WHALES MAX LENGTH >= 80.0 FEET

# Prep list
long_whales = [columns] # add column names as first row

for whale in whales[1:]:
    if float(whale[columns.index('max_length_feet')]) >= 80.0:
        long_whales.append(whale)

# Write to file
path = 'noaa_whales_long_length.csv'
write_csv(path, long_whales)


# 4.3 FILTER ON WHALES BETWEEN 40 AND 70 TONS (INCLUSIVE)

# Prep list
mid_weight_whales = [columns] # add column names as first row

for whale in whales[1:]:
    if 40.0 <= float(whale[columns.index('max_weight_tons')]) <= 70.0:
        mid_weight_whales.append(whale)

# Write to file
path = 'noaa_whales_mid_weight.csv'
write_csv(path, mid_weight_whales)



# 5.0 ADDITIONAL FUN

# Note: csv has a Sniffer class that can check if a csv has headers.
# See https://docs.python.org/3/library/csv.html#csv.Sniffer

def read_csv_2(path, delimiter=',', has_columns=True):
    """TODO"""

    columns = []
    data = []

    with open(path, 'r', newline='', encoding='utf-8') as csv_file:
        reader = csv.reader(csv_file, delimiter=delimiter)

        # Check if 1st row comprises column names
        if has_columns:
            columns = reader.__next__() # return 1st row, advance to next row

        # Get row data
        for row in reader:
            data.append(row)

        return (columns, data) # tuple


# 5.1 WHALES MAX LIFESPAN > 70 YEARS

# Call function
columns, whales = read_csv_2(NOAA_WHALES) # unpack

long_lived_whales = [columns]

# No longer need to slice whales list
for whale in whales:
    if float(whale[columns.index('max_lifespan_years')]) > 70.0:
        long_lived_whales.append(whale)

# Write to file (OPEN IN EXCEL)
path = 'noaa_whales_long_lived.csv'
write_csv(path, long_lived_whales)
