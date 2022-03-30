try:
    input = input('input: ')
    if int(input):
        print("Enter the project")
except ValueError:
    if not input:
        print('this is an empty file')
    else:
        print("the file contains: ", input)
