#Program to shuffle numbers from the given list using random module
import random

n = [15,20,38,45,10,5]
print("Original list = ",n)
random.shuffle(n)
print("Shuffled list = ",n)