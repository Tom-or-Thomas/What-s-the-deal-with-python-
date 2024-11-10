
numbers = range(1, 30)

file_path = './src/assets/test.txt'
# Used for resource management (files, database, etc.).
# Want to write to a file.
with open(file_path, 'w') as file: 
    string = ','.join(str(x) for x in numbers)
    file.write(string)
    file.write('\nThis is the begging of a our Python legacy...')
    file.close()


# Appending stuff to the file
with open(file_path, 'a') as file:
    file.write('\nThis should be added to the bottom of the file')


# Reading file
with open(file_path, 'r') as file: 
    print('This is what is in the file', file.read())
    file.close()



