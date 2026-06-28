import random


def human_turn(sticks_left):
    while True:
        try:
            take = int(input(f"Take matches from 1 t o3 only, my dear, there are only {sticks_left} matches left"))
            if 1<=take<=min(3,stick_left):
                return take
            else:
                print("You only can take from 1 to 3 matches at the time")
        except ValueError:
            print("ERROR, type THE NUMBER")

def comp_turn(sticks_left):
    if sticks_left >= 4 and stick_left%4 != 0:
        comp_take = sticks_left%4
    else:
        comp_take = random.randint(1, min(3, stick_left))
    print(f"Comp takes {comp_take} matches! Keep up)")
    return comp_take
            
