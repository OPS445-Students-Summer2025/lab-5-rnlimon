#!/usr/bin/env python3
# Author ID: rnlimon

def read_file_string(file_name):
    # Takes file_name as string for a file name, returns its entire contents as a string
    f = open(file_name,'r')
    data = f.read()    # Read the entire contents of the file as a string
    f.close()
    return data   # Return the file contents

def read_file_list(file_name):
    # Takes a file_name as string for a file name,
    f = open(file_name, 'r')   # Open - file in read mode
    lines_new = list(f)   # Read all lines into a list (includes newline characters)

    # return its entire contents as a list of lines without new-line characters
    lines = []
    for line in lines_new:
        lines.append(line.strip())  # Remove newline characters and add to the list
    f.close()
    return lines

def append_file_string(file_name, string_of_lines):
    # Takes two strings, appends the string to the end of the file
    f = open(file_name, 'a')    # Open - file in append mode
    f.write(string_of_lines)    # Write the string to the end of the file
    f.close()

def write_file_list(file_name, list_of_lines):
    # Takes a string and list, writes all items from list to file where each item is one line
    f = open(file_name, 'w')   # Open the file in write mode (overwrites existing content)
    for line in list_of_lines:
        f.write(line + '\n')   # Write each line followed by a newline character
    f.close()

def copy_file_add_line_numbers(file_name_read, file_name_write):
    # Takes two strings, reads data from first file, writes data to new file, adds line number to new file
    current_list = read_file_list(file_name_read)
    write_new = open(file_name_write, 'w')

    line_number = 1
    for line in current_list:
        line_with_number = str(line_number) + ':' + line + '\n'    # Prefix line number to each line
        write_new.write(line_with_number)  # Write the numbered line to the new file
        line_number = line_number + 1   # Increment line number

if __name__ == '__main__':
    file1 = 'seneca1.txt'
    file2 = 'seneca2.txt'
    file3 = 'seneca3.txt'
    string1 = 'First Line\nSecond Line\nThird Line\n'
    list1 = ['Line 1', 'Line 2', 'Line 3']
    append_file_string(file1, string1)
    print(read_file_string(file1))
    write_file_list(file2, list1)
    print(read_file_string(file2))
    copy_file_add_line_numbers(file2, file3)
    print(read_file_string(file3))