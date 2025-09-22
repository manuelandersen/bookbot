import sys
from stats import count_words, count_characters_appearances, sort_characters_dictionary

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

def main():

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    file = get_book_text(book_path)
    num_words = count_words(file)
    num_of_characters = count_characters_appearances(file)
    characters = sort_characters_dictionary(num_of_characters)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for dict in characters:
        print(f"{dict["char"]}: {dict["num"]}")
    print("============= END ===============")

main()
