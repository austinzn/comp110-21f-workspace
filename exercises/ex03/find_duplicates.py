"""Finding duplicate letters in a word."""

__author__ = "730466197"

word: str = input("Enter a word: ")
letter: str = ""
dupe: str = ""
bank: int = 0
i: int = 0
n: int = 0


while i < len(word):
    letter = word[i]
    while n < len(word):
        if letter == word[n]:
            bank = bank + 1
        n = n + 1
    n = 0
    i = i + 1
if bank > len(word):
    dupe = "True"
else:
    dupe = "False"
print("Found duplicate: " + dupe)