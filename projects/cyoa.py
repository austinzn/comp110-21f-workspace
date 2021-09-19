"""Choose your own adventure project."""

import random

points: float
player: str
smiley: str = "\U0001F604" 
scream: str = "\U0001F631"
scared: str = "\U0001F628"
cry: str = "\U0001F62A"


def main() -> None:
    """A game about your cats weight."""
    global points
    points = 8.0
    greet()

    choice: int
    path: str

    begin: str = (input("Type \"start\" to begin game: "))
    while begin == "start":
        points = round(points, 2)
        print(f"Your cat weighs {points} pounds.")
        if points <= 4 and points > 2:
            print(f"Your cat is unhealthily underweight... {scream}")
        if points > 4 and points < 12:
            print(f"Your cat is at a healthy weight {smiley}.")
        if points > 12:
            print(f"Your cat is getting overweight... {scream}")
        if points < 2:
            print(f"Your cat died of exhaustion and starvation. {cry}")
        if points > 20:
            print(f"Your cat is getting super chunky... {scared}")
        if points > 25:
            print(f"Your cat died from being too fat. Yikes {cry}")
        print("What would you like to do with your cat?")
        print("1. Feed your cat.")
        print("2. Play with your cat.")
        print("3. Exit game.")
        choice = int(input("Enter the number of your choice: "))
        if choice == 1:
            path = str(input("Do you want to feed your cat a lot, a moderate amount, or a little food? "))
            if path == "a lot":
                points = points + random.uniform(.6, .8)
                print("You fed your cat a lot of food and it gained some weight.")
            elif path == "a moderate amount":
                points = points + random.uniform(.3, .5)
                print("You fed your cat a moderate amount of food and it  gained some weight..")
            elif path == "a little":
                points = points + random.uniform(.05, .2)
                print("You fed your cat a little food and it gained some weight..")
            else:
                print("Please choose either \"a lot\" \"a moderate amount or\" \"a little\"")
        if choice == 2:
            path = str(input("Do you want to play with your cat a lot, a moderate amount, or a little food? "))
            if path == "a lot":
                points = points - random.uniform(.3, .5)
                print("You played with your cat a lot and it lost some weight.")
            elif path == "a moderate amount":
                points = points - random.uniform(.1, .25)
                print("You played with your cat a moderate amount and it lost some weight..")
            elif path == "a little":
                points = points - random.uniform(0, .1)
                print("You played with your cat a little and it lost some weight.")
            else:
                print("Please choose either \"a lot\" \"a moderate amount or\" \"a little\"")
        if choice == 3:
            print(f"Your cat weighed {points} pounds.")
            print("Thanks for playing!")
            begin = ""
        else:
            print("Please choose either 1, 2, or 3.")


def greet() -> None:
    global player
    player = input("What is your name? ")
    print(f"Greetings {player}! This game is about taking care of your pet cat. Choose to feed it or play with it and keep track of your cat's weight!!")


if __name__ == "__main__":
    main()