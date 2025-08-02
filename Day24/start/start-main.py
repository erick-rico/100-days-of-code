# with open("file.txt") as f:
#     contents = f.read()
#     print(contents)

with open("file.txt", mode='a') as f:
    f.write("\nNew text.")

with open("new_file.txt", mode='w') as f:
    f.write("New text.")
