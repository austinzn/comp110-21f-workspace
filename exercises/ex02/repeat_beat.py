"""Repeating a beat in a loop."""

<<<<<<< HEAD
__author__ = "730466197"
=======
__author__ = "730243388"
>>>>>>> bfe00d0bc5e66cd0a568dfd7048add409d018ba1


# Begin your solution here...
beat: str = input("What beat do you want to repeat? ")
<<<<<<< HEAD
repeat: int = int(input("How many times do you want to repeat it? "))
integer: int = 0
full_beat: str = ""

if repeat > 0:
    while integer < (repeat - 1):
        full_beat = beat + " " + full_beat
        integer = integer + 1
    full_beat = full_beat + beat
    print(full_beat)
else:
    print("No beat...")
=======
number: int = int(input("How many times do you want to repeat it? "))
i: int = 0
if (number < 1):
    print("No beat...")
else:
    print_beat = beat
    while (i < number - 1):
        print_beat += "" + beat

    print(print_beat)
>>>>>>> bfe00d0bc5e66cd0a568dfd7048add409d018ba1
