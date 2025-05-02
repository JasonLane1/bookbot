from stats import word_counter


def main(converted_book_to_string):
    print(converted_book_to_string)



def get_book_text():
    with open("/home/jason/workspace/github.com/bootdev/bookbot/books/frankenstein.txt") as raw_book_import:
        converted_book_to_string = raw_book_import.read()
        return converted_book_to_string
    

print(f"{word_counter(get_book_text)} words found in the document")
