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


            
