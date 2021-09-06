"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730466197"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


# Begin your solution here...
quote: str = ""

print("Your fortune cookie says...")
integer: int = randint(1, 3)
if integer == 1:
    quote = "You will soon find love."
else:
    if integer == 2:
        quote = "You will have a blessed evening."
    else:
        qoute = "Great riches will find you in the future."
print(quote)
print("Now, go spread positive vibes!")