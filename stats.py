def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def words_num(file_contents):
    words_list = file_contents.split()
    return len(words_list)

def count_characters(file_contents):
    words_list = file_contents.split()
    characters_dic = {}
    for i in range(0, len(words_list)):
        word = words_list[i].lower()
        char = list(word)
        for j in range(0, len(char)):
            try:
                characters_dic[char[j]] = characters_dic[char[j]] + 1
            except KeyError:
                characters_dic[char[j]] = 1

    return characters_dic

def print_report(characters_dic):    
    items_list = [{"char" : char, "num" : num} for char,num in characters_dic.items()]
    sorted_items = sorted(items_list, key=lambda item: item["num"], reverse=True)
    return sorted_items

           

