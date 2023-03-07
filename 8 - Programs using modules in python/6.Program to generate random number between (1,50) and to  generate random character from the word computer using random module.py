#Program to generate random number between (1,50) and to  generate random character from the word computer using random module

import random

n = random.randint(1,50)
print("Random nmber = ",n)

c = random.choice("computer")
print("Random character = ",c)