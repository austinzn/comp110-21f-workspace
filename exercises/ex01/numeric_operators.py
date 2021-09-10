"""Practice for numeric operators, type conversion, and string concatenation."""

__author__ = "730466197"

left = int(input("What is on the left-hand side? "))
right = int(input("What is on the right-hand side? "))
print("Left-hand side: " + str(left))
print("Right-hand side: " + str(right))
print(str(left) + " ** " + str(right) + " is " + str(left ** right))
print(str(left) + " / " + str(right) + " is " + str(left / right))
print(str(left) + " // " + str(right) + " is " + str(left // right))
print(str(left) + " % " + str(right) + " is " + str(left % right))