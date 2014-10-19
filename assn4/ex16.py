def monty_choice(player_choice, prize_door):
    monty_door = 1
    if monty_door != player_choice and monty_door != prize_door:
        print ("I am opening door #1")
    if monty_door == player_choice:
        if prize_door == 2:
            print ("I am opening door #3")
        elif prize_door == 3:
            print ("I am opening door #2")
    if monty_door == prize_door:
        if player_choice == 2:
            print ("I am opening door #3")
        elif player_choice == 3:
            print ("I am opening door #2")
