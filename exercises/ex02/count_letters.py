"""Counting letters in a string."""

<<<<<<< HEAD
__author__ = "730466197"


# Begin your solution here...
letter: str = input("What letter do you want to search for?: ")
word: str = input("Enter a word: ")
count: int = 0
i: int = 0

while i < len(word):
    if word[i] == letter:
        count = count + 1
    i = i + 1
=======
__author__ = "730243388"


# Begin your solution here...

letter: str = input("What letter do you want to seach for? ")
word: str = input("Enter a word ")
count: int = 0
i: int = 0
while (i < len(word)):
    if word[i] == letter:
        count += 1
    i += 1
>>>>>>> bfe00d0bc5e66cd0a568dfd7048add409d018ba1
print("Count: " + str(count))
