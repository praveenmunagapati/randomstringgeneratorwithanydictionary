import re
def load_words():
    with open('words.txt') as word_file:
        valid_words = list(sorted(set(word_file.read().split())))

    return valid_words

cleanlist = []

if __name__ == '__main__':
    english_words = load_words()
    for i in english_words:
        if re.search(r"[\d+'\-\.\&\,\/]+", i):
            pass
        else:
            if(len(i)>4 and len(i) < 6):
                cleanlist.append(i)

    """for i in cleanlist:
        print(i)"""

    """print(len(cleanlist))
    for i in range(len(cleanlist)):
        print(i)"""

    dictionary = {}
    dictionary = dict(enumerate(cleanlist))
    #print(dictionary)

    for i in dictionary:
        print()







