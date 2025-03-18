def get_number_of_words(book_content):
    words = book_content.split()
    return len(words), words

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

def convert_dict_to_list(chars_occurrences_count):
    characters_as_list = []
    for alphabet_in_text in chars_occurrences_count:
        characters_as_list.append({"name": alphabet_in_text, "value": chars_occurrences_count[alphabet_in_text]})
    
    return characters_as_list
