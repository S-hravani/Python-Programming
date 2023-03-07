#program to find the list of words that are longer than  n frroma given list of words

def long_words(n,str):
    word_list = []
    txt = str.split()
    for x in txt:
        if len(x)>n:
            word_list.append(x)
    return word_list

print(long_words(3,"The quick brown fox jumps over the lazy dog"))

