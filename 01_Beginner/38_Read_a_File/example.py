try:
    with open('/Users/onurcatik/Library/CloudStorage/OneDrive-Personal/Python/01_Beginner/38_Read_a_File/text.txt', 'r') as file:
        for line in file:
            print(line, end='')
except FileNotFoundError:
    print("The file was not found.")