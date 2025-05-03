

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
    for char in concat_raw.lower():
        if char in my_dict.keys():
            my_dict[char] += 1
        else:
            my_dict[char] = 1
    return my_dict


def sort_my_dict(my_dict):
    sorted_dict = {"char": "", "num": ""}
    for x, y in my_dict.items():
        sorted_dict["char"] = x
        sorted_dict["num"] = y
        print(sorted_dict)
    return sorted_dict
    