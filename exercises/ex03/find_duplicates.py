"""Finding duplicate letters in a word."""

<<<<<<< HEAD
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
=======
__author__ = "123456789"

word: str = input("Enter a word: ")

i: int = 0
duplicate: bool = False
while (i < len(word)):
    j: int = i + 1
    while(j < len(word)):
        if (word[i] == word[j]):
            duplicate = True
        j += 1
    i += 1

print("Found duplicate: " + str(duplicate))
>>>>>>> bfe00d0bc5e66cd0a568dfd7048add409d018ba1
