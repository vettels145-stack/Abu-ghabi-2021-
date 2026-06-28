from utils import winner_winner_chicken_dinner
from applog import human_turn, comp_turn
import time

def start_game():
    sticks = 21
    turn = input("Wanna be first? (YES/NO) - ").strip().lower()
    if turn == "yes" or turn == "да":
        human_first = True
    else:
        human_first = False
        print("You were suppose to type yes or да, not some random syllables, ok?")
    play_game(human_first, sticks)

def play_game(human_first, sticks):
    current_pl = human_first
    while sticks > 0:
        if current_pl:
            taken = human_turn(sticks)
        else:
            taken = comp_turn(sticks)
        sticks -= taken
        current_pl = not current_pl
        if winner_winner_chicken_dinner(sticks):
            winner = "YOU ARE THE WORLD CHAMPION! THE WORLD CHAMPION! MAX!" if current_pl else "Lewis won, history rewrited"
            print(winner)
            break
if __name__ == "__main__":
    import random
    start_game()

#time.sleep(10)










































        
