def get_book(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()

    return file_contents


def count_words(text):
    
    words = text.split()

    return len(words)

def count_characters(text):

    characters = {}
    for chr in text:
        chr = chr.lower()
        if chr in characters:
            characters[chr] += 1
        else:
            characters[chr] = 1
    
    return characters


def sort_on(dict):
    return dict["num"]


def sorted_chrs(txt_characters):
    sorted_list = []

    for chr in txt_characters:
        sorted_list.append({"char": chr, "num":txt_characters[chr]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


def number_of_appearances_sorted(txt):
    txt_characters = count_characters(txt)
    sorted_chr = sorted_chrs(txt_characters)
    return sorted_chr


def create_report():
    path_to_file = "books/frankenstein.txt"
    book_name = path_to_file.replace("books/", "").replace(".txt", "").capitalize()
    txt = get_book(path_to_file)
    txt_words = count_words(txt)
    chrs_sorted = number_of_appearances_sorted(txt)

    print(f"\n----Beginning of the report for the book: {book_name}----\n")
    print(f"Total number of words: {txt_words}\n")
    print(f"Number of appearances of every character: \n")

    for chr in chrs_sorted:
        if not chr["char"].isalpha():
            continue
        print(f"Character: '{chr['char']}' was found: {chr['num']} times")
    
    print(f"\n----Ending of the report for the book: {book_name}----\n")



def main():
    return create_report()


if __name__ == '__main__':

    main()