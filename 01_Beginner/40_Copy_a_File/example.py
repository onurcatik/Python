import shutil

# Define the source and destination file paths
source_file = '/Users/onurcatik/Library/CloudStorage/OneDrive-Personal/Python/01_Beginner/40_Copy_a_File/test.txt'
destination_file = '/Users/onurcatik/Library/CloudStorage/OneDrive-Personal/Python/01_Beginner/40_Copy_a_File/copy.txt'

# Copy the contents of the source file to the destination file
shutil.copyfile(source_file, destination_file)

print(f"File copied from {source_file} to {destination_file}")
