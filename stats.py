def sort_on(items):
    return items["num"]

def get_num_words(text):
    num_words = text.split()

    return len(num_words)

def get_num_characters(text):
    characters = dict()
    for word in text:
        char = word.lower()
        if char not in characters:
            characters[char] = 1
        else:
            characters[char] += 1
    return characters


def show_reports(text_dict, count):
    new_list = []
    for d in text_dict:
        if d.isalpha():
            new_list.append({"char":d, "num":text_dict[d] })
    
    new_list.sort(reverse=True, key=sort_on)



    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    for l in new_list:
        print(f"{l['char']}: {l['num']}")
    print("============= END ===============")
  