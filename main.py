import sys
from stats import word_counter, sorting_dict

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count -----------")

    total_words = word_counter(book_path)
    print(f"Found {total_words} total words")

    print("----------- Character Count -----------")
    char_list = sorting_dict(book_path)
    for char in char_list:
        print(f"{char['char']}: {char['num']}")

    print("============= END ===============")

if __name__ == "__main__":
    main()
