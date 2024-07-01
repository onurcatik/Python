import os

path = r'/Users/onurcatik/Library/CloudStorage/OneDrive-Personal/Python/01_Beginner/37_File_Detection/test.txt'

# Check if the path exists
if os.path.exists(path):
    if os.path.isfile(path):
        print("That is a file.")
    elif os.path.isdir(path):
        print("That is a directory.")
else:
    print("The location doesn't exist.")