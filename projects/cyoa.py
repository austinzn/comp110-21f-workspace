"""Choose your own adventure project."""

points: float
player: str


def main() -> None:
    """A game about your cats weight."""
    global points
    points = 8.0
    greet()

    choice: int
    feed: str
    play: str

    begin: str = (input("Type \"start\" to begin game: "))
    while begin == "start":
        points = round(points, 2)
        print(f"Your cat weighs {points} pounds.")
        if points <= 4 and points > 2:
            print("Your cat is unhealthily underweight...")
        if points < 4 and points > 12:
            print("Your cat is at a healthy weight")
        if points > 12:
            print("Your cat is getting overweight...")
        if points < 2:
            print("Your cat died of exhaustion and starvation. Take better care of it next time. :(")
        if points > 20:
            print("Your cat is getting super chunky...")
        if points > 30:
            print("Your cat died from being too fat. Yikes")
        print("What would you like to do with your cat?")
        print("1. Feed your cat.")
        print("2. Play with your cat.")
        print("3. Exit game.")
        choice = int(input("Enter the number of your choice: "))
        if choice == 1:
            feed = str(input("Do you want to feed your cat a lot, a moderate amount, or a little food? "))
            if feed == "a lot":
                points = points + 0.7
                print("You fed your cat a lot of food.")
            elif feed == "a moderate amount":
                points = points + .5
                print("You fed your cat a moderate amount of food.")
            elif feed == "a little":
                points = points + .2
                print("You fed your cat a little food.")
            else:
                print("Please choose either \"a lot\" \"a moderate amount or\" \"a little\"")
        if choice == 2:
            feed = str(input("Do you want to play with your cat a lot, a moderate amount, or a little food? "))
            if feed == "a lot":
                points = points - .5
                print("You played with your cat.")
            elif feed == "a moderate amount":
                points = points - .3
                print("You played with your cat a moderate amount.")
            elif feed == "a little":
                points = points - .1
                print("You played with your cat a little.")
            else:
                print("Please choose either \"a lot\" \"a moderate amount or\" \"a little\"")
        if choice == 3:
            print(f"Your cat weighed {points} pounds.")
            print("Thanks for playing!")
            begin = ""
        if choice != 1 or choice != 2 or choice != 3:
            print("Please choose either 1, 2, or 3.")


def greet() -> None:
    global player
    player = input("What is your name? ")
    print(f"Greetings {player}! This game is about taking care of your pet cat. Choose to feed it or play with it and see how your cat ends up!")


if __name__ == "__main__":
    main()