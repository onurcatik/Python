import os

def move_file_or_directory(source, destination):
    try:

        if not os.path.exists(source):
            raise FileNotFoundError(f"Source '{source}' was not found.")

        if os.path.exists(destination):
            print(f"There is already a file or directory at '{destination}'.")
        else:

            os.replace(source, destination)
            print(f"'{source}' was moved to '{destination}'.")
    except FileNotFoundError as e:
        print(e)
    except Exception as e:
        print(f"An error occurred: {e}")

source_file = r'/Users/onurcatik/Library/CloudStorage/OneDrive-Personal/Python/01_Beginner/41_Move_a_File/file.txt'
destination_file = r'/Users/onurcatik/Library/CloudStorage/OneDrive-Personal/Python/file.txt'
move_file_or_directory(source_file, destination_file)

source_dir = r'C:\path\to\your\source\folder'
destination_dir = r'C:\path\to\your\destination\folder'
move_file_or_directory(source_dir, destination_dir)