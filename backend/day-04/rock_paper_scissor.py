Player_1 = input("Player1: ").lower()
Player_2 = input("Player2: ").lower()

if (Player_1 == "rock") and (Player_2 == "scissor"):
    print(f"Player 1 wins!\n ```````")
elif (Player_1 == "rock") and (Player_2 == "paper"):
    print(f"Player 2 wins!\n ```````")
elif (Player_1 == "rock") and (Player_2 == "rock"):
    print(f"It's a tie!\n ```````")
elif (Player_1 == "paper") and ( Player_2 == "paper"):
    print(f"It's a tie!\n ```````")
elif (Player_1 == "paper") and (Player_2 == "scissor"):
    print(f"Player 2 wins!\n ```````")
elif (Player_1 == "paper") and (Player_2 == "rock"):
    print(f"Player 1 wins!\n ```````")
elif (Player_1 == "scissor") and (Player_2 == "scissor"):
    print(f"It's a tie!\n ```````")
elif (Player_1 == "scissor") and (Player_2 == "paper"):
    print(f"Player 1 wins!\n ```````")
elif (Player_1 == "scissor") and (Player_2 == "rock"):
    print(f"Player 2 wins!\n ```````")
