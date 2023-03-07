#Program to check whether given key is already exists in a dictionary

d = {1:10,2:20,3:30,4:40,5:50}
def is_key_present(x):
    if x in d:
        print("key is present in dictionary")
    else:
        print("key is not present in dictionary")

is_key_present(3)
is_key_present(6)
