"""Repeating a beat in a loop."""

__author__ = "730466197"


# Begin your solution here...
beat: str = input("What beat do you want to repeat? ")
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
