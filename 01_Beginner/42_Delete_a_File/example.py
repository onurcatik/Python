import os
import shutil

def delete_file(path):
    try:
        os.remove(path)
        print(f"{path} was deleted")
    except FileNotFoundError:
        print("File not found")
    except PermissionError:
        print("You do not have permission to delete this file")

def delete_empty_directory(path):
    try:
        os.rmdir(path)
        print(f"{path} was deleted")
    except FileNotFoundError:
        print("Directory not found")
    except PermissionError:
        print("You do not have permission to delete this directory")
    except OSError as e:
        print(f"Error: {e}")

def delete_directory_with_contents(path):
    try:
        shutil.rmtree(path)
        print(f"{path} was deleted")
    except FileNotFoundError:
        print("Directory not found")
    except PermissionError:
        print("You do not have permission to delete this directory")
    except OSError as e:
        print(f"Error: {e}")


delete_file("test.txt")
delete_empty_directory("empty_folder")
delete_directory_with_contents("folder")