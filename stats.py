

#Counts words in string
def word_counter(raw_string):
    counter = 0
    split_string_list = raw_string().split()
    for word in split_string_list:
        counter += 1
    return counter


#Counts characters inside of the string, placing them into a dictionary
def character_counter(raw_string):
    my_dict = {}
    concat_raw = raw_string().replace(" ", "").replace("\n", "")
    
    return concat_raw