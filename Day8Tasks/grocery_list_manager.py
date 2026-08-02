items = []

print("Enter grocery items one at a time.")
print("Type 'done' when you're finished.\n")

while True:
    item = input("Enter item: ")
    if item.lower() == "done":
        break
    items.append(item)

with open("grocery.txt", "w") as file:
    for item in items:
        file.write(item + "\n")

print("\nGrocery list saved successfully!")

print("\nContents of grocery.txt:")
with open("grocery.txt", "r") as file:
    print(file.read())
    