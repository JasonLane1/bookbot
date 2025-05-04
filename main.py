from stats import word_counter
from stats import character_counter
from stats import sort_my_dict
import sys

args = sys.argv

len_args = len(args)
if len_args < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
elif len_args > 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text():
    with open(f"/home/jason/workspace/github.com/bootdev/bookbot/{args[1]}") as raw_book_import:
        converted_book_to_string = raw_book_import.read()
        return converted_book_to_string
    

my_dict_ = character_counter(get_book_text)


print("============ BOOKBOT ============")
print(f"Analyzing book found at {args[1]}...")
print("----------- Word Count ----------")
print(f"Found {word_counter(get_book_text)} total words")
print("--------- Character Count -------")
sorted_dict_ = sort_my_dict(my_dict_)
print("============= END ===============")