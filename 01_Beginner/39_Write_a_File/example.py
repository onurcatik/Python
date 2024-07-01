text = "Yo\nThis is some text.\nHave a good one!"
with open('test.txt', 'w') as file:
    file.write(text)
print("File has been written.")

# Appending to the file
additional_text = "\nHave a nice day!\nSee ya!"
with open('test.txt', 'a') as file:
    file.write(additional_text)
print("Text has been appended.")

# Overwriting the file
new_text = "Uh oh, this text has been overwritten!"
with open('test.txt', 'w') as file:
    file.write(new_text)
print("File has been overwritten.")