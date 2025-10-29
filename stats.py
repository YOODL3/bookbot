def get_book_text(path):
    with open(path, "r", encoding="utf-8") as file:
        return file.read()

def word_counter(path):
    text = get_book_text(path)
    words = text.split()
    return len(words)

def char_counter(path):
    text = get_book_text(path).lower()
    characters = {}

    for c in text:
        if c.isalpha():
            characters[c] = characters.get(c, 0) + 1

    return characters

def sorting_dict(path):
    char_dict = char_counter(path)
    char_list = [{"char": char, "num": count} for char, count in char_dict.items()]
    char_list.sort(key=lambda x: x["num"], reverse=True)
    return char_list



# File path (hardcoded) just to test = /home/yoodle/workspace/github.com/YOODL3/bookbot/books/frankenstein.txt