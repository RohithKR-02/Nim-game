def calculate_nim_sum(piles):
    from functools import reduce
    from operator import xor
    return reduce(xor, piles)

def display_piles(piles):
    print("\nCurrent Piles:")
    for i, pile in enumerate(piles):
        print(f"Pile {i+1}: {pile}")
    print()

def player_move(piles):
    while True:
        try:
            pile_index = int(input("Choose a pile (1, 2, 3...): ")) - 1
            if pile_index not in range(len(piles)) or piles[pile_index] == 0:
                print("Invalid pile. Try again.")
                continue
            remove_count = int(input(f"How many to remove from pile {pile_index+1}? "))
            if 1 <= remove_count <= piles[pile_index]:
                piles[pile_index] -= remove_count
                break
            else:
                print("Invalid number of objects to remove.")
        except ValueError:
            print("Invalid input, enter numbers only.")

def ai_move(piles):
    nim_sum = calculate_nim_sum(piles)
    for i in range(len(piles)):
        target = piles[i] ^ nim_sum
        if target < piles[i]:
            removed = piles[i] - target
            print(f"AI removes {removed} from pile {i+1}")
            piles[i] = target
            return
    # No winning move, just take one from the first non-empty pile
    for i in range(len(piles)):
        if piles[i] > 0:
            print(f"AI removes 1 from pile {i+1}")
            piles[i] -= 1
            return

def is_game_over(piles):
    return all(p == 0 for p in piles)

def nim_game():
    print("Welcome to Nim Game!")
    piles = [3, 4, 5]  # You can customize pile sizes
    player_turn = True

    while not is_game_over(piles):
        display_piles(piles)
        if player_turn:
            print("Your turn:")
            player_move(piles)
        else:
            print("AI's turn:")
            ai_move(piles)
        player_turn = not player_turn

    display_piles(piles)
    if player_turn:
        print("AI wins!")
    else:
        print("You win!")

# Start the game
nim_game()
