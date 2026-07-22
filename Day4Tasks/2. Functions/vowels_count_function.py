def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

a = "chaitanya"
print(f"Number of vowels in '{a}' is {count_vowels(a)}")
