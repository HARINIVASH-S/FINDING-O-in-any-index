old=[' ',' ','O']

def old_list(game):
    print(f"The list is: {game}")

from random import shuffle

def shuf(game):
    shuffle(game)
    return game

def player_choise():
    index = 'a'
    while index not in ['0','1','2']:
        index = input("Your options are [0, 1, 2]. Pick one: ")
    return int(index)

def check(game, choise):
    if game[choise] == 'O':
        print("🎉 You win!")
    else:
        print("❌ You lose!")

def play():
    opp = 'a'
    while opp not in ['Y','N']:
        opp = input("Do you want to play? (Y or N): ").upper()
        if opp not in ['Y','N']:
            print("Invalid choice")

    if opp == 'Y':
        print("🎮 The game starts now!")
        print("The rules are simple:")
        print("Guess where the 'O' is hiding among three positions [0, 1, 2].")

        start = True
        old = [' ', ' ', 'O']
        while start:
            old_list(['?', '?', '?'])  # Hide real values
            old = shuf(old)
            index = player_choise()
            check(old, index)
            old_list(old)  # Show where 'O' was
            start = play()  # Recurse

    else:
        print("Thanks for playing!")
        return False

# 🟢 Start the game here
play()
