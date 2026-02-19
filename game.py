import random

print("Welcome to snakes and ladders!")

position1 = 0
position2 = 0
dice_moves = 0
position_history1 = []
position_history2 = []

current_player = 1

while True:

    input(f"\nPlayer {current_player}, press enter to roll the dice: ")
    dice = random.randint(1, 6)
    dice_moves += 1
    print(f"Player {current_player} rolled a {dice}")

    # Select correct player position
    if current_player == 1:
        position = position1
    else:
        position = position2

    # ✅ FIXED OVERSHOOT LOGIC
    if position + dice > 100:
        print("You need exact number to reach 100! No move.")
    else:
        position += dice
        print(f"You moved to position {position}")

        choice = input("(ladder/snake/nothing)=> ").lower()

        if choice == "ladder":
            position += dice
            print(f"You climbed a ladder of {dice}! Now at {position}")
        elif choice == "snake":
            position -= 2 * dice
            if position < 0:
                position = 0
            print(f"Snake bite! Now at {position}")

    # Save back to correct player
    if current_player == 1:
        position1 = position
        position_history1.append(position1)
    else:
        position2 = position
        position_history2.append(position2)

    # ✅ WIN CHECK
    if position == 100:
        print(f"\n🎉 Player {current_player} wins!")
        print(f"Total dice rolls: {dice_moves}")
        print(f"Player 1 history: {position_history1}")
        print(f"Player 2 history: {position_history2}")
        break

    # 🔄 SWITCH PLAYER
    current_player = 2 if current_player == 1 else 1
