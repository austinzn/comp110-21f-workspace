"""Choose your own adventure project."""

__author__ = "730466197"

import random

points: float
player: str
begin: str
smiley: str = "\U0001F604" 
scream: str = "\U0001F631"
scared: str = "\U0001F628"
cry: str = "\U0001F62A"


def main() -> None:
    """A game about your cats weight."""
    global points
    global begin
    points = 8.0
    greet()

    begin = (input("Type \"start\" to begin game: "))
    while begin == "start":
        points = round(points, 2)
        print(f"{player}'s cat weighs {points} pounds.")
        if points <= 4 and points > 2:
            print(f"{player}'s cat is unhealthily underweight... {scream}")
        if points > 4 and points < 12:
            print(f"{player}'s cat is at a healthy weight {smiley}.")
        if points > 12:
            print(f"{player}'s cat is getting overweight... {scream}")
        if points < 2:
            print(f"{player}'s cat died of exhaustion and starvation. {cry}")
        if points > 20:
            print(f"{player}'s cat is getting super chunky... {scared}")
        if points > 25:
            print(f"{player}'s cat died from being too fat. Yikes {cry}")
        print(f"What will {player} do?")
        print("1. Feed their cat.")
        print("2. Play with their cat.")
        print("3. Exit game.")
        points = points + options(int(input("Enter the number of your choice: ")))
        

def options(x: int) -> float:
    """Determines which path to go down based on the choice made."""
    global begin
    global points
    global player
    change: float
    path: str

    if x == 1:
        path = str(input(f"Should {player} feed their cat a lot, a moderate amount, or a little food? "))
        if path == "a lot":
            change = random.uniform(.6, .8)
            print(f"{player} fed their cat a lot of food and it gained some weight...")
            return change
        elif path == "a moderate amount":
            change = random.uniform(.3, .5)
            print(f"{player} fed their cat a moderate amount of food and it gained some weight...")
            return change
        elif path == "a little":
            change = random.uniform(.05, .2)
            print(f"{player} fed their cat a little food and it gained some weight...")
            return change
        else:
            print("Please choose either \"a lot\" \"a moderate amount or\" \"a little\"")
            return float(0.0)
    if x == 2:
        path = str(input(f"Should {player} play with their cat a lot, a moderate amount, or a little food? "))
        if path == "a lot":
            change = random.uniform(-.5, -.3)
            print(f"{player} played with their cat a lot and it lost some weight...")
            return change
        elif path == "a moderate amount":
            change = random.uniform(-.25, -.1)
            print(f"{player} played with their cat a moderate amount and it lost some weight...")
            return change
        elif path == "a little":
            change = random.uniform(-.1, 0)
            print(f"{player} played with their cat a little and it lost some weight...")
            return change
        else:
            print("Please choose either \"a lot\" \"a moderate amount or\" \"a little\"")
            return float(0.0)
    if x == 3:
        print(f"{player}'s cat weighed {points} pounds.")
        print("Thanks for playing!")
        begin = "Finished"
        return float(0.0)
    else:
        print("Please choose either 1, 2, or 3.")
        return float(0.0)


def greet() -> None:
    """Greets the player when they begin the program."""
    global player
    player = input("Hello! Before we start, enter a player name: ")
    print(f"Greetings {player}! In this game, you play as someone who owns a pet cat. Choose to feed it or play with it and keep track of your cat's weight!!")


if __name__ == "__main__":
    main()