def start_game():
    sticks = 21
    turn = input("Wanna be first? (YES/NO) - ").strip().lower()
    if turn == "yes" or turn == "да":
        human_first = True
    else:
        human_first = False
    play_game(human_first, sticks)












































        
