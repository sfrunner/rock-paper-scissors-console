import random

VALID_CHOICES = ['rock', 'paper', 'scissors', 'arm laser']
CLASSIC_CHOICES = ['rock', 'paper', 'scissors']

def get_computer_choice():
    """Randomly selects rock, paper, scissors, or arm laser for the computer."""
    return random.choice(VALID_CHOICES)

def determine_winner(player_choice, computer_choice):
    """Determines the winner of a round."""
    if player_choice == computer_choice:
        return 'tie'

    # Arm laser beats rock, paper, and scissors
    if player_choice == 'arm laser' and computer_choice in CLASSIC_CHOICES:
        return 'player'
    if computer_choice == 'arm laser' and player_choice in CLASSIC_CHOICES:
        return 'computer'

    winning_combinations = {
        'rock': 'scissors',
        'paper': 'rock',
        'scissors': 'paper'
    }

    if winning_combinations[player_choice] == computer_choice:
        return 'player'
    else:
        return 'computer'

def display_result(player_choice, computer_choice, result):
    """Displays the result of a round."""
    print(f"\nYou threw: {player_choice.upper()}")
    print(f"Computer threw: {computer_choice.upper()}")
    
    if result == 'tie':
        print("It's a TIE!")
    elif result == 'player':
        print("You WIN this round!")
    else:
        print("Computer WINS this round!")

def main():
    """Main game loop."""
    player_wins = 0
    computer_wins = 0
    ties = 0
    
    print("=" * 50)
    print("Welcome to Rock Paper Scissors!")
    print("=" * 50)
    print("\nValid choices: rock, paper, scissors, arm laser (beats all)")
    print("Type 'quit' to exit the game\n")
    
    while True:
        # Get player choice
        player_choice = input("What do you throw down? ").lower().strip()
        
        # Check if player wants to quit
        if player_choice == 'quit':
            print("\n" + "=" * 50)
            print("Final Score:")
            print(f"  You: {player_wins} wins")
            print(f"  Computer: {computer_wins} wins")
            print(f"  Ties: {ties}")
            print("=" * 50)
            print("Thanks for playing!")
            break
        
        # Validate player choice
        if player_choice not in VALID_CHOICES:
            print("Invalid choice! Please enter 'rock', 'paper', 'scissors', or 'arm laser'.")
            continue
        
        # Get computer choice and determine winner
        computer_choice = get_computer_choice()
        result = determine_winner(player_choice, computer_choice)
        
        # Display result
        display_result(player_choice, computer_choice, result)
        
        # Update win counts
        if result == 'player':
            player_wins += 1
        elif result == 'computer':
            computer_wins += 1
        else:
            ties += 1
        
        # Display current score
        print(f"\nCurrent Score - You: {player_wins} | Computer: {computer_wins} | Ties: {ties}")
        print("-" * 50)

if __name__ == "__main__":
    main()

