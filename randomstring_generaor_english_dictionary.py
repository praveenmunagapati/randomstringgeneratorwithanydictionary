import re
#put any disctionary words lin words.txt 
def load_words():
    
    with open('words.txt') as word_file:
        #cleans and deduplicates 
        valid_words = list(sorted(set(word_file.read().split())))

    return valid_words


cleanlist = []

if __name__ == '__main__':
    english_words = load_words()
    for i in english_words:
        #furthur cleaning words containing -,.\& digits 
        if re.search(r"[\d+'\-\.\&\,\/]+", i):
            pass
        else:
            if(len(i)>4 and len(i) < 6):
                cleanlist.append(i)

   #if you want to print shoot yourself and uncomment              
    """for i in cleanlist:
        print(i)"""

    """print(len(cleanlist))
    for i in range(len(cleanlist)):
        print(i)"""

    
    dictionary = {}
    dictionary = dict(enumerate(cleanlist))
    #print(dictionary)


    # import random
    import random
    randomstringlist = []
    # prints a random value from the list
    for i in range(100000):
        randomstring = (random.choice(cleanlist)+
        random.choice(cleanlist)+
        random.choice(cleanlist))
        if(len(randomstring)<20):
            randomstringlist.append(randomstring.lower())

    #checking to see any duplicate string arrises 
    #simulated test 1 million strings no duplicates 
    #so far good 
   
    print(len(randomstringlist))
    print(len(list(set(randomstringlist))))

    #happy coding





