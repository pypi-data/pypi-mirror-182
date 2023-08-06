from termcolor import cprint 
from termcolor import colored
import sys

W = "Wumpus"
P = "Pit"
T = "Treasure"
S = "Start"
found_treasure = False

map = [
    [S, 0, 0, 0], 
    [W, 0, 0, T], 
    [0, 0, P, 0], 
    [0, 0, 0, P]]
start_state = (0,0)

def shape(map):
    s = map[0]
    return (len(s),len(map))
def begin():
    cprint("            Welcome to wumpus world".upper(),"red")
    cprint("""
    The world has the following contents
    a. There is a monster named "Wumpus" which is very hungry and eats whatever comes to it's path.
    b. There are multiple pits which are bottomless and once someone falls into it, there is only way and it's down.
    c. There is a marvelous treasure hidden somewhere in this world between all these pits and giant monster.

    To win the game, find the treasure and retieve it back.

    As the locations are all very dark, we will provide with hints about the environment to help you go to the goal.
    
    The hints that will be provided are as follows:
    a. STRENCH - If there is a wumpus in an adjacent room from the present room.
    b. BREEZE  - If there is a pit in an adjacent room from the present room.

    Click Yes as soon as you are ready.
    ""","cyan")

    cprint("GOOD LUCK","cyan")
    



def actions(map,state):
    x_cord, y_cord = state 
    all_actions = [
        (x_cord + 1, y_cord),
        (x_cord - 1, y_cord),
        (x_cord, y_cord + 1),
        (x_cord, y_cord - 1)
    ]
    possible_actions = []
    for x,y in all_actions:
        if 0 <= x < shape(map)[0] and 0 <= y < shape(map)[1]:
            possible_actions += [(x,y)]
    return possible_actions


def hint(map,state):
    for x,y in actions(map,state):
        if map[x][y] == W:
            cprint("STENCH","red")
        if map[x][y] == P:
            cprint("BREEZE","blue")
        print()


def evaluate(map,state,found_treasure):
    x_cord, y_cord = state 
    if map[x_cord][y_cord] == W:
        cprint("The wumpus ate you","red")
        sys.exit()
    if map[x_cord][y_cord] == P:
        cprint("You are falling in an endless pit","red")
        cprint("NOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO","red")
        sys.exit()
    if map[x_cord][y_cord] == T:
        cprint("You found the treasure!","yellow")
        found_treasure = True 
    if map[x_cord][y_cord] == S and found_treasure:
        cprint("You won","yellow")
        sys.exit()
    cprint("You are safe","green")
    return found_treasure
    
def terminal(map,state,found_treasure):
    x_cord, y_cord = state 
    if map[x_cord][y_cord] == W or map[x_cord][y_cord] == P:
        return True 
    if map[x_cord][y_cord] == S and found_treasure:
        return True

def play(state,found_treasure):
    print("The hints for the present state are:")
    hint(map, state)
    print("Please enter the tile you want to move to, the following are the possible options:")
    print(actions(map,state))
    new_state = list(int(i) for i in input().split())
    found_treasure = evaluate(map,new_state,found_treasure)
    return new_state,found_treasure
    
def game(state,found_treasure):
    while not terminal(map,state,found_treasure):
        state,found_treasure = play(state,found_treasure)


def start():
    begin()
    game(start_state,found_treasure)


start()
