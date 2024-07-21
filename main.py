def sort_on(dict):
    return dict["value"]

def convert_dict_to_list(chars_occurrences_count):
    characters_as_list = []
    for alphabet_in_text in chars_occurrences_count:
        characters_as_list.append({"name": alphabet_in_text, "value": chars_occurrences_count[alphabet_in_text]})
    
    return characters_as_list

def count_chars(words_in_book):
    chars_occurrences_count = {}
    
    for word in words_in_book:
        for character in word:
            if character.isalpha():    
                if character in chars_occurrences_count:
                    chars_occurrences_count[character] += 1
                else :
                    chars_occurrences_count[character] = 1
    
    return chars_occurrences_count

def get_number_of_words(book_content):
    words = book_content.split()
    return len(words), words


def get_book_content(file_path):
    with open(file_path) as book_to_read :
        return book_to_read.read() 


def main():
    file_path = "books/frankenstein.txt"
    
    book_content = get_book_content(file_path)
    book_content = book_content.lower()
    
    words_in_book_count, words_in_book = get_number_of_words(book_content)
    
    chars_occurrences_count_dict = count_chars(words_in_book)
    characters_as_list = convert_dict_to_list(chars_occurrences_count_dict)
    characters_as_list.sort(reverse=True, key=sort_on)
    
    print(f"=== Begin report of {file_path} ===")
    print(f"{words_in_book_count} words in book")
    
    print()

    for char_data in characters_as_list:
        print(f"The '{char_data['name']}' character was found {char_data['value']} times")
    
    print()

    print("=== End of Report ===")

main()