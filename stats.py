def count_words(book_file):
    words = book_file.split()
    return len(words)

def count_characters_appearances(book_file):
    words = book_file.upper().lower()
    characters = list(words)
    dict = {}
    for character in characters:
        if character not in dict:
            dict[character] = 1
        else:
            dict[character] += 1

    return dict

def sort_characters_dictionary(dict):
    list = []
    for character in dict:
        list.append({"char": character, "num": dict[character]})
    
    def sort_on(items):
        return items["num"]
    
    list.sort(reverse=True, key=sort_on)

    return list