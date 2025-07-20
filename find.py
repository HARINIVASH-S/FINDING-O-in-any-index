old=[' ',' ','O']

def old_list(game):
    print(f"the  list is :{game}")

from random import shuffle

def shuf(game):
    shuffle(game)
    return game

def player_choise():
    index='a'
    while index not in ['0','1','2']:
        index=input("you options are [0,1,2] pick one : ")
    return int(index)

def check(game,choise):
    if(game[choise]=='O'):
        print("you win")
    else:
        print("you loss")


def play():
    opp='a'
    while opp not in ['Y','N']:
        opp=input("Did you want to play again (Y or N): ")

        if opp not in ['Y','N']:
            print("invalid choise")
    if (opp=='Y'):
        print("the game start now ")
        print("The rules are simple:")
        print("you want to find the O it can be in any index position and you can select one index position then if it matches you won go and enjoy it")
        start=True
        old=[' ',' ','O']
        while start:
            old_list(old)
            old=shuf(old)
            index=player_choise()
            check(old,index)
            old_list(old)
            start=play()
    else :
        return False         
        