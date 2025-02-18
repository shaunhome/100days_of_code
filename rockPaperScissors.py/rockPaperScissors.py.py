player_one_input = str(input("Play:"))
player_two_input = str(input("play"))

def rps(player_one_input, player_two_input):
    if player_one_input == player_two_input:
    print("drawer")
    elif player_one_input == "rock" and player_two_input == "paper":
        print("player 2 win")
    elif player_one_input == "rock" and player_two_input == "scissors" or 
    player_one_input == "scissors" and player_two_input == "paper":
    print("player 1 wins")
else:
    print("Player 2 wins")