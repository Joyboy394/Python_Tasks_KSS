try:
    with open("notes.txt", "r") as file:
        contents = file.read()
        print(contents)
except FileNotFoundError:
    print("notes.txt not found. Please make sure the file exists in the same folder as this program.")
    