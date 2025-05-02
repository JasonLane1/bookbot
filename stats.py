

#Counts words in string
def word_counter(raw_string):
    counter = 0
    split_string_list = raw_string().split()
    for word in split_string_list:
        counter += 1
    return counter