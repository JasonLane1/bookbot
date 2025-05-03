from stats import word_counter
from stats import character_counter
from stats import sort_my_dict


def main(converted_book_to_string):
    print(converted_book_to_string)



def get_book_text():
    with open("/home/jason/workspace/github.com/bootdev/bookbot/books/frankenstein.txt") as raw_book_import:
        converted_book_to_string = raw_book_import.read()
        return converted_book_to_string
    

my_dict_ = character_counter(get_book_text)


print("============ BOOKBOT ============")
print("Analyzing book found at books/frankenstein.txt...")
print("----------- Word Count ----------")
print(f"Found {word_counter(get_book_text)} total words")
print("--------- Character Count -------")
sorted_dict_ = sort_my_dict(my_dict_)
print("============= END ===============")