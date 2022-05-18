
sentences_list = [
    "hey, evidence for the domestication of food crops and animals,",
    "Before understanding metaclasses, you need to master classes in Python hey?",
    "We will Skype and discuss technical post your submission.",
    "Make sure that you have have given the google drive link to your assignment solution in the google form hey.",
    "And Python has a very peculiar idea of what classes are, borrowed from the Smalltalk language!"
]
separators = ['.',',','!','?',]
my_dict = {}

def make_hashmap():
    for i,sentence in enumerate(sentences_list):
        for word in sentence.split(" "):
            if word[-1] in separators:
                word = word[:-1]

            index_list = my_dict.get(word)
            if index_list:
                index_list.append(i)
                my_dict[word] = index_list

            else:
                my_dict[word] = [i]
    

def search(word:str):
    index_list = my_dict.get(word)

    if index_list:
        return [sentences_list[i] for i in index_list]

    return index_list

make_hashmap()

print(search("lol"))
print(search("hey"))
