from stats import *
import sys

def sort_on(dict):
    return dict["value"]



def get_book_content(file_path):
    with open(file_path) as book_to_read :
        return book_to_read.read() 


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_path = sys.argv[1]
    
    book_content = get_book_content(file_path)
    
    book_content = book_content.lower()
    
    words_in_book_count, words_in_book = get_number_of_words(book_content)
    
    chars_occurrences_count_dict = count_chars(words_in_book)
    characters_as_list = convert_dict_to_list(chars_occurrences_count_dict)
    characters_as_list.sort(reverse=True, key=sort_on)
    
    print("============ BOOKBOT ============")

    print("Analyzing book found at books/frankenstein.txt...")

    print("----------- Word Count ----------")

    print(f"Found {words_in_book_count} total words")

    print("--------- Character Count -------")

    for char_data in characters_as_list:
        print(f"{char_data['name']}: {char_data['value']}")

    print("============= END ===============")

main()