#Write a program to find longest word

def longest_word(filename):
    with open (filename, "r") as fp:
        words = fp.read().split()
    max_len = len(max(words, key=len))
    return [word for word in words if len(word) == max_len]

print(longest_word("demo.txt"))
