try:
    with open("article.txt", "r") as file:
        content = file.read()

    lines = content.splitlines()
    words = content.split()

    line_count = len(lines)
    word_count = len(words)
    char_count = len(content)

    print(f"Number of lines: {line_count}")
    print(f"Number of words: {word_count}")
    print(f"Number of characters: {char_count}")

except FileNotFoundError:
    print("article.txt not found. Please make sure the file exists in the same folder as this program.")
    