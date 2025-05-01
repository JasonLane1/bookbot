
def main(converted_book_to_string):
    print(converted_book_to_string)



def get_book_text():
    with open("/home/jason/workspace/github.com/bootdev/bookbot/books/frankenstein.txt") as raw_book_import:
        converted_book_to_string = raw_book_import.read()
        return converted_book_to_string
    

def word_counter(raw_string):
    counter = 0
    split_string_list = raw_string().split()
    for word in split_string_list:
        counter += 1
    return counter

print(f"{word_counter(get_book_text)} words found in the document")
